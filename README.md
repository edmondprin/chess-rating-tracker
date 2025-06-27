# Chess.com Rating Tracker 🧠♟️

A Python script that fetches and logs your Chess.com blitz and rapid ratings using the public Chess.com API. Great for tracking progress over time and visualizing rating trends.

## Features

- Pulls your current **rapid** and **blitz** ratings
- Saves ratings with timestamp to a local CSV file
- Designed for scheduled automation using `cron`
- Clean, lightweight, and easy to extend

## Example Output

Rapid Rating: 1324
Blitz Rating: 1289

## Files

- `chess_rating_tracker.py`: Main script
- `chess_ratings.csv`: Output file with historical data

## Usage

1. Clone the repo or copy the script
2. Install dependencies:

```bash
pip install requests pytz
```
3. Run the script
```bash
python3 chess_rating_tracker.py
```
## (Optional) Set up a cron job to log ratings daily (macOS / Linux)

Edit the crontab: 
```bash
crontab -e
```

Add a line like this to run every day at 7 PM (make sure to update the path to match your 
local environment)::
```bash
0 19 * * * /usr/bin/python3 /full/path/to/chess_rating_tracker.py
```

## License

MIT

## Author

@edmondprin
