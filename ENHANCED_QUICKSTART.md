"""
Enhanced OmniRecon Platform - Quick Start Guide
Author: Frank Arthur
Version: 3.0.0
"""

# OmniRecon Enhanced Platform - Quick Start Guide

## 🚀 What's New in Enhanced OmniRecon

The enhanced OmniRecon platform now includes advanced features from the Advanced Scanner project:

### ✨ New Features

1. **AI-Powered Pattern Recognition**
   - Enhanced username analysis with bot detection
   - Jaccard and Levenshtein similarity algorithms
   - Detailed characteristic analysis (length, numbers, special chars, etc.)
   - Suspicious keyword detection

2. **Advanced Risk Scoring Engine**
   - 5-factor weighted risk assessment:
     - Social Presence (25%)
     - Data Breaches (30%)
     - Suspicious Patterns (20%)
     - Platform Diversity (15%)
     - Profile Activity (10%)
   - Configurable risk thresholds
   - Detailed risk factor breakdown

3. **Real-Time Monitoring and Alerts**
   - Automatic alert generation for critical findings
   - Multiple alert severity levels (INFO, WARNING, HIGH, CRITICAL)
   - Alert types: high risk, critical risk, multiple breaches, suspicious patterns, bot detection
   - Real-time alert tracking and summaries

4. **Interactive HTML Dashboard**
   - Collapsible sections for better organization
   - Progress bars for risk visualization
   - Hover effects and smooth animations
   - Alert display with severity indicators
   - Pattern analysis visualization

5. **Comprehensive API Key Management**
   - Secure storage of API keys
   - Support for 11+ services (Shodan, VirusTotal, HaveIBeenPwned, etc.)
   - Environment variable configuration
   - Key masking for security
   - Import/export functionality

6. **Enhanced Social Media Investigation**
   - Support for 17+ platforms
   - Profile data extraction
   - Concurrent scanning
   - Detailed results with status codes

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/frank814/omnirecon.git
cd omnirecon

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## 🔑 API Key Configuration

### Option 1: Using Configuration File

```python
from omnirecon.config.api_keys import APIKeyManager

# Initialize API key manager
api_manager = APIKeyManager()

# Set API keys
api_manager.set_api_key("shodan", "your_shodan_api_key")
api_manager.set_api_key("virustotal", "your_virustotal_api_key")

# View configured keys (masked)
print(api_manager.get_all_keys())
```

### Option 2: Using Environment Variables

```bash
export OMNIRECON_SHODAN_API_KEY="your_shodan_api_key"
export OMNIRECON_VIRUSTOTAL_API_KEY="your_virustotal_api_key"
export OMNIRECON_HAVEIBEENPWNED_API_KEY="your_hibp_api_key"
```

Then in your code:

```python
from omnirecon.config.api_keys import APIKeyManager

api_manager = APIKeyManager()
api_manager.configure_from_env()
```

## 🎯 Basic Usage

### Command Line Interface

```bash
# Basic username scan
python -m omnirecon.main --username frank814

# Generate enhanced HTML report
python -m omnirecon.main --username frank814 --output html

# Generate all report formats
python -m omnirecon.main --username frank814 --output all

# Verbose output with custom settings
python -m omnirecon.main --email user@example.com --verbose --max-workers 20
```

### Python API

```python
from omnirecon.core.orchestrator import Orchestrator
from omnirecon.core.risk_scoring import RiskScoringEngine
from omnirecon.core.real_time_monitor import RealTimeMonitor

# Initialize orchestrator
orchestrator = Orchestrator()

# Run scan
results = orchestrator.scan("frank814", "username")

# Calculate risk score
risk_engine = RiskScoringEngine()
risk_assessment = risk_engine.calculate_risk(results)

# Monitor for alerts
monitor = RealTimeMonitor()
alerts = monitor.monitor_scan(results)

print(f"Risk Score: {risk_assessment['risk_score']}")
print(f"Risk Level: {risk_assessment['risk_level']}")
print(f"Alerts Generated: {len(alerts)}")
```

## 📊 Enhanced Reporting

### Interactive HTML Dashboard

```python
from omnirecon.reporting.enhanced_html_report import EnhancedHTMLReport

# Generate enhanced HTML report
report = EnhancedHTMLReport()
html_content = report.generate(results, "scan_report.html")
```

The enhanced HTML report includes:
- Collapsible sections
- Risk score progress bar
- Alert display with severity indicators
- Pattern analysis visualization
- Interactive hover effects

### Alert System

```python
from omnirecon.core.real_time_monitor import RealTimeMonitor, AlertSeverity

# Initialize monitor
monitor = RealTimeMonitor()

# Get all alerts
all_alerts = monitor.get_alerts()

# Get critical alerts only
critical_alerts = monitor.get_alerts(AlertSeverity.CRITICAL)

# Get alert summary
summary = monitor.get_alert_summary()
print(f"Total alerts: {summary['total_alerts']}")
print(f"By severity: {summary['by_severity']}")
```

## 🔍 Pattern Recognition

```python
from omnirecon.modules.ai.pattern_recognition_module import PatternRecognitionModule

# Initialize pattern recognition
pattern_module = PatternRecognitionModule()

# Analyze username
analysis = pattern_module.analyze("frank814")

print(f"Characteristics: {analysis['characteristics']}")
print(f"Patterns found: {analysis['patterns']}")
print(f"Risk indicators: {analysis['risk_indicators']}")
print(f"Confidence: {analysis['confidence']}")

# Calculate similarity between usernames
similarity = pattern_module.calculate_similarity("frank814", "frank_814")
print(f"Similarity: {similarity:.2f}")
```

## 🎨 Risk Assessment

```python
from omnirecon.core.risk_scoring import RiskScoringEngine, RiskLevel

# Initialize risk engine
risk_engine = RiskScoringEngine()

# Calculate risk
risk_assessment = risk_engine.calculate_risk(results)

print(f"Risk Score: {risk_assessment['risk_score']}")
print(f"Risk Level: {risk_assessment['risk_level']}")
print(f"Assessment: {risk_assessment['assessment']}")

# View risk factors
for factor in risk_assessment['risk_factors']:
    print(f"{factor['name']}: {factor['score']} - {factor['description']}")
```

## 🌐 Social Media Investigation

```python
from omnirecon.modules.social.social_media_module import SocialMediaModule

# Initialize social media module
social_module = SocialMediaModule()

# Run investigation
results = social_module.run("frank814")

print(f"Platforms checked: {results['summary']['total_checked']}")
print(f"Accounts found: {results['summary']['found']}")

# View platform results
for platform, data in results['platforms'].items():
    if data['found']:
        print(f"{platform}: {data['url']}")
```

## ⚙️ Configuration

### Risk Scoring Configuration

```python
from omnirecon.core.risk_scoring import RiskScoringEngine

# Custom risk weights
config = {
    "weights": {
        "social_presence": 30,
        "data_breaches": 25,
        "suspicious_patterns": 20,
        "platform_diversity": 15,
        "profile_activity": 10
    },
    "thresholds": {
        "low": 0,
        "medium": 30,
        "high": 60,
        "critical": 80
    }
}

risk_engine = RiskScoringEngine(config)
```

### Alert Thresholds

```python
from omnirecon.core.real_time_monitor import RealTimeMonitor

# Custom alert thresholds
config = {
    "thresholds": {
        "high_risk": 70.0,
        "critical_risk": 85.0,
        "multiple_breaches": 2,
        "suspicious_patterns": 1
    }
}

monitor = RealTimeMonitor(config)
```

## 📚 Supported Services

### API Key Services
- Shodan (Internet devices)
- VirusTotal (Malware analysis)
- HaveIBeenPwned (Data breaches)
- Censys (Internet intelligence)
- SecurityTrails (DNS intelligence)
- Hunter (Email finder)
- EmailRep (Email reputation)
- Twitter (Social media)
- GitHub (Code hosting)
- Reddit (Social media)
- LinkedIn (Professional network)

### Social Media Platforms
- Twitter/X
- Instagram
- Facebook
- LinkedIn
- GitHub
- Reddit
- YouTube
- TikTok
- Pinterest
- Spotify
- Steam
- Twitch
- Discord
- Medium
- DeviantArt
- Flickr
- Vimeo

## 🛡️ Security and Ethics

⚠️ **Important**: OmniRecon is designed for AUTHORIZED, ETHICAL OSINT ONLY.

Always:
- Obtain proper authorization before scanning
- Respect privacy and legal boundaries
- Use results for legitimate security purposes
- Follow ethical guidelines and best practices

## 📞 Support

For issues, questions, or suggestions:
- GitHub: https://github.com/frank814/omnirecon
- Issues: https://github.com/frank814/omnirecon/issues

## 📄 License

MIT License - See LICENSE file for details.

---

**Author**: Frank Arthur  
**GitHub**: https://github.com/frank814  
**Version**: 3.0.0