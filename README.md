# Pet Food Subscription Demo

A demo project that includes:
1. A subscription-based pet food delivery service website with LaunchDarkly integration for A/B testing
2. Testing utilities for generating sample data and testing LaunchDarkly variations

## Environment Variables

The project requires two different LaunchDarkly SDK keys:

| Variable | Description | Used In |
|----------|-------------|----------|
| LAUNCHDARKLY_CLIENT_KEY | Client-side SDK key for the website | server.py (injected into script.js) |
| LAUNCHDARKLY_SDK_KEY | Server-side SDK key for testing | variation_test.py |

Set these environment variables before running the respective components:

```bash
# Bash/Zsh
export LAUNCHDARKLY_CLIENT_KEY=your-client-side-key
export LAUNCHDARKLY_SDK_KEY=your-server-side-key

# Windows Command Prompt
set LAUNCHDARKLY_CLIENT_KEY=your-client-side-key
set LAUNCHDARKLY_SDK_KEY=your-server-side-key

# Windows PowerShell
$env:LAUNCHDARKLY_CLIENT_KEY="your-client-side-key"
$env:LAUNCHDARKLY_SDK_KEY="your-server-side-key"
```

## Website Demo

### Features

- Responsive landing page design
- Interactive trial signup modal
- LaunchDarkly integration for A/B testing
- Feature sections highlighting service benefits
- "How It Works" section
- Local development server

### Website Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd pet-food-subscription
```

2. Set up LaunchDarkly:
- Set the LAUNCHDARKLY_CLIENT_KEY environment variable
- Create a feature flag named `hero-banner-test` in your LaunchDarkly dashboard with the following structure:
```json
{
  "image": "URL to banner image",
  "heading": "Banner heading text",
  "subtext": "Banner subtext"
}
```

### Running the Website

Start the local development server:

```bash
python3 server.py
```

The server will:
- Start on http://localhost:3000
- Automatically inject your LaunchDarkly client key into script.js
- Display a warning if LAUNCHDARKLY_CLIENT_KEY is not set

To stop the server, press Ctrl+C in the terminal.

## Testing Utilities

The project includes two Python scripts for testing LaunchDarkly functionality:

### 1. Data Generation Script (generate_data.py)

Generates test data for LaunchDarkly experiments:

- Creates 100 records with the format:
```
"convert_to_paid","user","<UUID>","",<TIMESTAMP>
```
- Saves unique context keys to a separate file
- Useful for creating test data sets

Usage:
```bash
python3 generate_data.py
```

Outputs:
- event_data.csv: Contains the full event data
- context_keys.txt: List of unique context keys

### 2. Variation Test Script (variation_test.py)

Tests LaunchDarkly flag evaluations:

- Reads context keys from context_keys.txt
- Makes variation_detail calls for a boolean flag named "hero-image"
- Includes microsecond delays between calls
- Logs detailed results of each evaluation

Setup:
```bash
# Install dependencies
pip install -r requirements.txt

# Ensure LAUNCHDARKLY_SDK_KEY is set
echo $LAUNCHDARKLY_SDK_KEY  # Should show your server-side SDK key
```

Usage:
```bash
python3 variation_test.py
```

Output:
- Creates a timestamped log file (variation_results_YYYYMMDD_HHMMSS.log)
- Each log entry includes:
  * Timestamp
  * Context key
  * Flag value
  * Variation index
  * Evaluation reason

## Project Structure

```
pet-food-subscription/
├── index.html          # Main website
├── styles.css          # Website styles
├── script.js           # Website JavaScript with LD integration
├── server.py           # Local development server with env injection
├── generate_data.py    # Data generation utility
├── variation_test.py   # LD variation test utility
└── requirements.txt    # Python dependencies
```

## Technologies Used

- HTML5/CSS3/JavaScript
- LaunchDarkly Feature Management
  * Client-side SDK for website
  * Server-side SDK for testing
- Python
  * Local development server
  * Environment variable injection
  * Test data generation
  * Variation testing
