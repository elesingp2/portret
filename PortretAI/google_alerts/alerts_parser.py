from google_alerts import GoogleAlerts

# Environment variables or other secure methods should be used to store sensitive information
email = "elesin.gp@gmail.com"  # Replace with environment variable e.g., os.getenv('GOOGLE_ALERTS_EMAIL')
password = "k6q9N39j"  # Replace with environment variable e.g., os.getenv('GOOGLE_ALERTS_PASSWORD')

# Create an instance
ga = GoogleAlerts(email, password)

# Authenticate your user
ga.authenticate()

# List configured monitors
monitors = ga.list()
print("Monitors:", monitors)

# Example: Add a new monitor
new_monitor = ga.create("Hello World", {'delivery': 'RSS'})
print("Created Monitor:", new_monitor)

# Example: Modify an existing monitor
# Note: You need an actual monitor ID here
monitor_id = "example_monitor_id"
ga.modify(monitor_id, {'delivery': 'RSS', 'monitor_match': 'ALL'})

# Example: Delete a monitor
# Note: You need an actual monitor ID here
ga.delete(monitor_id)
