import os

# Set the directory where your video files are located
dir_path = r"C:\Users\Lidor\Downloads\Programs"

# Define a function to get the season and episode number from a file name
def get_episode_number(filename):
    filename_parts = filename.split('_')
    episode_info = filename_parts[1][1:]
    season_number = episode_info[0]
    episode_number = episode_info[1:]
    return season_number, episode_number

# Loop through all the files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.mp4') or filename.endswith('.mkv') or filename.endswith('.avi'):
        # Get the season and episode number from the file name
        season_number, episode_number = get_episode_number(filename)
        # Create a directory for the season if it doesn't already exist
        season_directory = os.path.join(dir_path, f'Season {season_number}')
        if not os.path.exists(season_directory):
            os.mkdir(season_directory)
        # Move the file to the season directory
        old_path = os.path.join(dir_path, filename)
        new_path = os.path.join(season_directory, filename)
        os.rename(old_path, new_path)
