# Pet Food Subscription Demo

A demo website for a subscription-based pet food delivery service, featuring LaunchDarkly integration for A/B testing the hero banner.

## Features

- Responsive landing page design
- Interactive trial signup modal
- LaunchDarkly integration for A/B testing
- Feature sections highlighting service benefits
- "How It Works" section
- Local development server

## Setup

1. Clone the repository:
```bash
git clone [repository-url]
cd pet-food-subscription
```

2. Configure LaunchDarkly:
- Replace `YOUR-SDK-KEY` in `script.js` with your LaunchDarkly SDK key
- Create a feature flag named `hero-banner-test` in your LaunchDarkly dashboard with the following structure:
```json
{
  "image": "URL to banner image",
  "heading": "Banner heading text",
  "subtext": "Banner subtext"
}
```

## Running Locally

Start the local development server:

```bash
python3 server.py
```

Visit http://localhost:3000 in your browser.

To stop the server, press Ctrl+C in the terminal.

## A/B Testing

The hero banner supports A/B testing through LaunchDarkly. You can configure different variations in your LaunchDarkly dashboard using the `hero-banner-test` feature flag.

Example variation:
```json
{
  "image": "https://example.com/new-banner.jpg",
  "heading": "Healthy, fresh food for your best friend",
  "subtext": "Try our personalized meal plans risk-free for 7 days"
}
```

## Project Structure

- `index.html` - Main HTML file
- `styles.css` - Stylesheet
- `script.js` - JavaScript with LaunchDarkly integration
- `server.py` - Local development server

## Technologies Used

- HTML5
- CSS3
- JavaScript
- LaunchDarkly Feature Management
- Python (for local development server)
