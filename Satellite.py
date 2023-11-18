import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels_status = "Inactive"
        self.data_collected = 0

    def rotate(self, direction):
        valid_directions = ["North", "South", "East", "West"]
        if direction not in valid_directions:
            raise ValueError(f"Invalid direction: {direction}. Valid directions are {valid_directions}")

        self.orientation = direction

    def activatePanels(self):
        if self.solar_panels_status == "Inactive":
            self.solar_panels_status = "Active"

    def deactivatePanels(self):
        if self.solar_panels_status == "Active":
            self.solar_panels_status = "Inactive"

    def collectData(self):
        if self.solar_panels_status == "Active":
            self.data_collected += 10


# Example usage with multiple lines of user input:
if __name__ == "__main__":
    try:
        satellite = Satellite()

        while True:
            # Get user input for commands
            user_input = input("Enter a command (rotate(direction), activatePanels(), deactivatePanels(), collectData()) or 'exit': ")

            if user_input.lower() == 'exit':
                break

            commands = user_input.strip().split('\n')

            for command in commands:
                try:
                    # Split command and arguments
                    parts = command.strip(')').split('(')
                    cmd = parts[0]
                    args = parts[1] if len(parts) > 1 else None

                    # Execute the command with arguments if present
                    if args:
                        getattr(satellite, cmd)(args)
                    else:
                        getattr(satellite, cmd)()
                except Exception as e:
                    logger.warning(f"Invalid command: {command}. Skipping. Error: {e}")

            # Display current state
            print(f'Orientation: "{satellite.orientation}"\n'
                  f'Solar Panels: "{satellite.solar_panels_status}"\n'
                  f'Data Collected: {satellite.data_collected}')

    except Exception as e:
        logger.error(f"An error occurred: {e}")
