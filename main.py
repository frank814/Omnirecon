"""
Main CLI Interface for OmniRecon
Author: Frank Arthur
Version: 3.0.0
"""

import argparse
import sys
from typing import Optional
from pathlib import Path

from omnirecon.core import Orchestrator, PluginManager
from omnirecon.reporting import JSONReport, HTMLReport, CSVReport, TXTReport
from omnirecon.utils import OmniReconLogger, Validators
from omnirecon.config import Settings


def print_banner() -> None:
    """Print professional ASCII banner."""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          OmniRecon – Modular OSINT Framework               ║
║                                                              ║
║          Version 3.0.0 | Author: Frank Arthur          ║
║          GitHub: https://github.com/frank814             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)


def print_legal_disclaimer() -> None:
    """Print legal disclaimer."""
    print(Settings.LEGAL_DISCLAIMER)
    
    response = input("\nDo you accept these terms? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("You must accept the terms to use OmniRecon.")
        sys.exit(0)


def create_parser() -> argparse.ArgumentParser:
    """
    Create argument parser for CLI.
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        prog="omnirecon",
        description="OmniRecon – Modular Open Source Intelligence Framework",
        epilog="Author: Frank Arthur | GitHub: https://github.com/frank814",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Target arguments
    target_group = parser.add_mutually_exclusive_group(required=True)
    target_group.add_argument(
        "--username",
        type=str,
        help="Username to investigate"
    )
    target_group.add_argument(
        "--email",
        type=str,
        help="Email address to investigate"
    )
    target_group.add_argument(
        "--phone",
        type=str,
        help="Phone number to investigate"
    )
    target_group.add_argument(
        "--domain",
        type=str,
        help="Domain to investigate"
    )
    
    # Output arguments
    parser.add_argument(
        "--output",
        choices=["json", "html", "csv", "txt", "all"],
        default="json",
        help="Output format (default: json)"
    )
    parser.add_argument(
        "--output-file",
        type=str,
        help="Output file path (default: auto-generated)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=Settings.DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {Settings.DEFAULT_OUTPUT_DIR})"
    )
    
    # Performance arguments
    parser.add_argument(
        "--max-workers",
        type=int,
        default=Settings.DEFAULT_MAX_WORKERS,
        help=f"Maximum concurrent workers (default: {Settings.DEFAULT_MAX_WORKERS})"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=Settings.DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {Settings.DEFAULT_TIMEOUT})"
    )
    
    # Logging arguments
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--log-file",
        type=str,
        help="Log file path (default: omnirecon.log)"
    )
    
    # Module arguments
    parser.add_argument(
        "--list-modules",
        action="store_true",
        help="List all available modules"
    )
    parser.add_argument(
        "--modules",
        type=str,
        nargs="+",
        help="Specific modules to run"
    )
    
    # Rate limiting arguments
    parser.add_argument(
        "--rate-limit",
        type=int,
        default=Settings.DEFAULT_RATE_LIMIT,
        help=f"Rate limit requests per minute (default: {Settings.DEFAULT_RATE_LIMIT})"
    )
    
    # Version argument
    parser.add_argument(
        "--version",
        action="version",
        version=f"OmniRecon {Settings.VERSION}"
    )
    
    return parser


def list_modules(plugin_manager: PluginManager) -> None:
    """
    List all available modules.
    
    Args:
        plugin_manager: Plugin manager instance
    """
    print("\nAvailable Modules:")
    print("=" * 70)
    
    metadata = plugin_manager.get_all_metadata()
    
    if not metadata:
        print("No modules loaded.")
        return
    
    for module_name, module_meta in metadata.items():
        print(f"\nModule: {module_name}")
        print(f"  Version: {module_meta.get('version', 'N/A')}")
        print(f"  Description: {module_meta.get('description', 'No description')}")
        
        if 'target_types' in module_meta:
            print(f"  Target Types: {', '.join(module_meta['target_types'])}")
        
        if 'enabled' in module_meta:
            status = "Enabled" if module_meta['enabled'] else "Disabled"
            print(f"  Status: {status}")


def generate_report(results: dict, output_format: str, 
                  output_file: Optional[str] = None,
                  output_dir: str = Settings.DEFAULT_OUTPUT_DIR) -> list:
    """
    Generate report in specified format(s).
    
    Args:
        results: OSINT scan results
        output_format: Output format (json, html, csv, txt, all)
        output_file: Optional output file path
        output_dir: Output directory
        
    Returns:
        list: List of generated file paths
    """
    generated_files = []
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate report based on format
    if output_format == "all":
        formats = ["json", "html", "csv", "txt"]
    else:
        formats = [output_format]
    
    for fmt in formats:
        # Get appropriate reporter
        if fmt == "json":
            reporter = JSONReport()
        elif fmt == "html":
            reporter = HTMLReport()
        elif fmt == "csv":
            reporter = CSVReport()
        elif fmt == "txt":
            reporter = TXTReport()
        else:
            continue
        
        # Generate output file path
        if output_file:
            file_path = output_file
        else:
            target = results.get("target", "unknown").replace("/", "_")
            file_path = str(output_path / f"{target}_report{reporter.get_extension()}")
        
        # Generate report
        reporter.generate(results, file_path)
        generated_files.append(file_path)
    
    return generated_files


def main() -> int:
    """
    Main entry point for OmniRecon CLI.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
    """
    # Print banner
    print_banner()
    
    # Print legal disclaimer
    print_legal_disclaimer()
    
    # Parse arguments
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize logger
    log_level = "DEBUG" if args.verbose else Settings.LOG_LEVEL
    logger = OmniReconLogger(
        log_file=args.log_file or Settings.LOG_FILE,
        log_level=getattr(__import__("logging"), log_level)
    )
    
    # Initialize orchestrator
    orchestrator = Orchestrator(
        max_workers=args.max_workers,
        timeout=args.timeout
    )
    
    # Load modules
    logger.info("Loading OmniRecon modules...")
    modules_loaded = orchestrator.load_modules()
    logger.info(f"Loaded {modules_loaded} modules")
    
    # List modules if requested
    if args.list_modules:
        list_modules(orchestrator.plugin_manager)
        return 0
    
    # Determine target
    if args.username:
        target = args.username
        target_type = "username"
    elif args.email:
        target = args.email
        target_type = "email"
    elif args.phone:
        target = args.phone
        target_type = "phone"
    elif args.domain:
        target = args.domain
        target_type = "domain"
    else:
        logger.error("No target specified")
        return 1
    
    # Validate target
    is_valid, error = Validators.validate_target(target)
    if not is_valid:
        logger.error(f"Invalid target: {error}")
        return 1
    
    # Log scan start
    logger.log_scan_start(target, target_type)
    
    # Run scan
    import time
    start_time = time.time()
    
    try:
        results = orchestrator.run_scan(target)
        
        duration = time.time() - start_time
        logger.log_scan_complete(target, duration)
        
        # Log risk assessment
        risk_assessment = results.get("risk_assessment", {})
        logger.log_risk_assessment(
            risk_assessment.get("risk_score", 0),
            risk_assessment.get("risk_level", "Unknown")
        )
        
        # Generate reports
        generated_files = generate_report(
            results,
            args.output,
            args.output_file,
            args.output_dir
        )
        
        # Log report generation
        for file_path in generated_files:
            logger.log_report_generated(args.output.upper(), file_path)
        
        # Print summary
        print("\n" + "=" * 70)
        print("SCAN COMPLETE")
        print("=" * 70)
        print(f"Target: {results.get('target', 'N/A')}")
        print(f"Target Type: {results.get('target_type', 'Unknown').title()}")
        print(f"Duration: {duration:.2f} seconds")
        
        scan_summary = results.get("scan_summary", {})
        print(f"Modules Executed: {scan_summary.get('modules_executed', 0)}")
        print(f"Modules Successful: {scan_summary.get('modules_successful', 0)}")
        print(f"Modules Failed: {scan_summary.get('modules_failed', 0)}")
        
        risk_assessment = results.get("risk_assessment", {})
        print(f"\nRisk Score: {risk_assessment.get('risk_score', 0)}/100")
        print(f"Risk Level: {risk_assessment.get('risk_level', 'Unknown')}")
        print(f"Assessment: {risk_assessment.get('assessment', 'N/A')}")
        
        print("\nGenerated Reports:")
        for file_path in generated_files:
            print(f"  - {file_path}")
        
        print("\n" + "=" * 70)
        
        return 0
        
    except KeyboardInterrupt:
        logger.warning("Scan interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Scan failed: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
