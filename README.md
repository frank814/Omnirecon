# OmniRecon – Modular Open Source Intelligence Framework

<div align="center">

![Version](https://img.shields.io/badge/version-3.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

**Modular Open Source Intelligence Framework**

Author: Frank Arthur | GitHub: [frank814](https://github.com/frank814)

</div>

---

## ⚠️ Legal Disclaimer

**OmniRecon is designed for AUTHORIZED, ETHICAL OSINT ONLY.**

By using this tool, you agree to:

1. Use only on targets you have permission to investigate
2. Respect all applicable laws and regulations
3. Use results for legitimate security purposes only
4. Not engage in any illegal or unauthorized activities
5. Protect the privacy of individuals and organizations

Unauthorized use is strictly prohibited and may result in legal consequences.

This tool is for educational and professional security research purposes only.

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Module Development](#-module-development)
- [Configuration](#-configuration)
- [Reporting](#-reporting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Capabilities

- **Modular Architecture**: Plugin-based system for easy extensibility
- **Multi-Target Support**: Investigate usernames, emails, phone numbers, and domains
- **Concurrent Processing**: ThreadPoolExecutor for efficient parallel execution
- **Risk Scoring Engine**: Weighted risk assessment with configurable thresholds
- **Multiple Output Formats**: JSON, HTML (dark theme), CSV, and TXT reports
- **Rate Limiting**: Built-in request throttling to respect service limits
- **Comprehensive Logging**: Detailed logging for transparency and debugging

### Security & Ethics

- Legal disclaimer on startup
- Input validation and sanitization
- Request timeout handling
- Respect for robots.txt where applicable
- No brute force or intrusive techniques
- Strictly operates on publicly accessible data

### Future AI Extensibility

- Identity correlation engine (planned)
- Pattern recognition (planned)
- Username similarity clustering (planned)
- Entity linking (planned)
- Anomaly detection (planned)

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install from Source

```bash
# Clone the repository
git clone https://github.com/frank814/omnirecon.git
cd omnirecon

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Quick Start

### Basic Usage

```bash
# Scan a username
python -m omnirecon.main --username frank814

# Scan an email
python -m omnirecon.main --email user@example.com

# Scan a phone number
python -m omnirecon.main --phone +1234567890

# Scan a domain
python -m omnirecon.main --domain example.com
```

### Generate Reports

```bash
# Generate HTML report
python -m omnirecon.main --username frank814 --output html

# Generate all report formats
python -m omnirecon.main --username frank814 --output all

# Specify custom output file
python -m omnirecon.main --username frank814 --output html --output-file my_report.html
```

### Advanced Options

```bash
# Verbose output with custom log file
python -m omnirecon.main --username frank814 --verbose --log-file scan.log

# Adjust performance settings
python -m omnirecon.main --username frank814 --max-workers 20 --timeout 60

# Rate limiting
python -m omnirecon.main --username frank814 --rate-limit 5

# List available modules
python -m omnirecon.main --list-modules
```

---

## 📖 Usage

### Command-Line Interface

OmniRecon provides a comprehensive CLI with the following options:

#### Target Arguments

- `--username`: Username to investigate
- `--email`: Email address to investigate
- `--phone`: Phone number to investigate
- `--domain`: Domain to investigate

#### Output Arguments

- `--output`: Output format (json, html, csv, txt, all)
- `--output-file`: Custom output file path
- `--output-dir`: Output directory (default: reports)

#### Performance Arguments

- `--max-workers`: Maximum concurrent workers (default: 10)
- `--timeout`: Request timeout in seconds (default: 30)

#### Logging Arguments

- `--verbose`: Enable verbose output
- `--log-file`: Custom log file path

#### Module Arguments

- `--list-modules`: List all available modules
- `--modules`: Specific modules to run

#### Rate Limiting

- `--rate-limit`: Rate limit requests per minute (default: 10)

#### Other

- `--version`: Show version information
- `--help`: Show help message

### Examples

```bash
# Comprehensive scan with all reports
python -m omnirecon.main --username target_user --output all --verbose

# Custom performance settings
python -m omnirecon.main --email target@example.com --max-workers 15 --timeout 45

# Rate-limited scan
python -m omnirecon.main --domain target.com --rate-limit 3

# Scan with specific modules
python -m omnirecon.main --username target_user --modules social_module email_module
```

---

## 📁 Project Structure

```
omnirecon/
│
├── core/                    # Core framework components
│   ├── __init__.py
│   ├── base_module.py      # Base class for all modules
│   ├── plugin_manager.py   # Module discovery and loading
│   ├── orchestrator.py     # Central orchestration engine
│   └── risk_scoring.py     # Risk assessment engine
│
├── modules/                # OSINT modules (extensible)
│   ├── social/            # Social media investigation
│   ├── email/             # Email analysis
│   ├── phone/             # Phone number lookup
│   ├── domain/            # Domain intelligence
│   ├── breach/            # Data breach checking
│   └── ai/                # Future AI modules
│
├── reporting/              # Report generation
│   ├── __init__.py
│   ├── json_report.py     # JSON report generator
│   ├── html_report.py     # HTML report generator (dark theme)
│   ├── csv_report.py      # CSV report generator
│   └── txt_report.py      # TXT report generator (executive summary)
│
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── logger.py          # Centralized logging
│   ├── validators.py      # Input validation
│   ├── network.py         # HTTP client with retry logic
│   └── rate_limiter.py    # Rate limiting
│
├── config/                 # Configuration
│   └── settings.py        # Centralized settings
│
├── api/                    # Optional REST API (planned)
│   └── server.py
│
├── main.py                 # CLI entry point
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🔧 Module Development

### Creating a Custom Module

All OmniRecon modules must inherit from the `BaseModule` class and implement the required methods:

```python
from omnirecon.core import BaseModule
from typing import Dict, Any

class CustomModule(BaseModule):
    """
    Custom OSINT module description.
    """
    
    def __init__(self):
        super().__init__()
        self.name = "CustomModule"
        self.version = "1.0.0"
        self.description = "Custom module for OSINT"
        self.enabled = True
        self.timeout = 30
        self.rate_limit = 10
    
    def initialize(self) -> bool:
        """
        Initialize the module.
        
        Returns:
            bool: True if initialization successful, False otherwise
        """
        # Perform initialization tasks
        return True
    
    def run(self, target: str) -> Dict[str, Any]:
        """
        Execute the module's main functionality.
        
        Args:
            target: The target to analyze
            
        Returns:
            Dict[str, Any]: Structured results from the module
        """
        # Perform OSINT operations
        results = {
            "found": False,
            "data": {}
        }
        
        return results
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get module metadata.
        
        Returns:
            Dict[str, Any]: Module information
        """
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "enabled": self.enabled,
            "target_types": ["username", "email"]
        }
```

### Module Best Practices

1. **Always validate input** before processing
2. **Respect rate limits** to avoid being blocked
3. **Handle errors gracefully** and return structured results
4. **Use the network client** for HTTP requests
5. **Log important events** for transparency
6. **Return structured dictionaries** for consistent reporting

---

## ⚙️ Configuration

### Risk Scoring Configuration

Risk scoring can be customized in `config/settings.py`:

```python
RISK_WEIGHTS = {
    "social_accounts": 15,
    "data_breach": 25,
    "email_security": 20,
    "domain_vulnerability": 20,
    "username_reuse": 10,
    "suspicious_pattern": 10
}

RISK_THRESHOLDS = {
    "low": 0,
    "medium": 25,
    "high": 50,
    "critical": 75
}
```

### Rate Limiting Configuration

```python
DEFAULT_RATE_LIMIT = 10  # requests per minute
DEFAULT_RATE_WINDOW = 60  # seconds
```

### Logging Configuration

```python
LOG_LEVEL = "INFO"
LOG_FILE = "omnirecon.log"
```

---

## 📊 Reporting

### Report Formats

OmniRecon supports multiple output formats:

#### JSON Report
Machine-readable format for programmatic processing

```bash
python -m omnirecon.main --username target --output json
```

#### HTML Report
Dark theme intelligence dashboard with visualizations

```bash
python -m omnirecon.main --username target --output html
```

#### CSV Report
Spreadsheet-ready format for data analysis

```bash
python -m omnirecon.main --username target --output csv
```

#### TXT Report
Executive summary for quick review

```bash
python -m omnirecon.main --username target --output txt
```

#### All Formats
Generate all report types at once

```bash
python -m omnirecon.main --username target --output all
```

### Report Contents

All reports include:

- Target information and type
- Scan summary (modules executed, success/failure counts)
- Risk assessment (score, level, factors)
- Detailed findings by category
- Timestamp and metadata

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP8 guidelines
- Add docstrings to all functions and classes
- Use type hints for better code clarity
- Write clean, readable code
- Test your changes thoroughly

### Module Contributions

When contributing new modules:

1. Inherit from `BaseModule`
2. Implement all required methods
3. Add comprehensive documentation
4. Include examples in the docstring
5. Test with various targets

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Frank Arthur**

- GitHub: [frank814](https://github.com/frank814)

---

## 🙏 Acknowledgments

- Built for the cybersecurity community
- Inspired by various OSINT tools and frameworks
- Thanks to all contributors and users

---

## ⚠️ Important Notice

**OmniRecon is NOT a hacking tool.** It is a professional OSINT framework for ethical, authorized, publicly available intelligence gathering.

Always:
- Obtain proper authorization before scanning
- Respect privacy and legal boundaries
- Use results for legitimate security purposes
- Follow ethical guidelines and best practices

---

## 📞 Support

For issues, questions, or suggestions:

- Open an issue on GitHub
- Check existing documentation
- Review the code examples

---

<div align="center">

**Made with ❤️ by Frank Arthur**

[GitHub](https://github.com/frank814) | [Issues](https://github.com/frank814/omnirecon/issues)

</div>
