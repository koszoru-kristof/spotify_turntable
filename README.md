# The Spotify Turntable

The Spotify Turntable is a project that aims to bring back the nostalgic feeling of playing music on a turntable while using the Spotify music streaming service. The project consists of a physical turntable that can be used to control the music currently plaing from Spotify. The turntable is equipped with a circular screen (ideally touchscreen) that displays the album art of the currently playing song. The user can interact with the turntable by rotating the platter to skip to the next or previous song, or by lifting the tonearm to pause or play the music among other features.

## Features

- **Physical Turntable**: The turntable is designed to look and feel like a traditional turntable, complete with a platter, tonearm, mounted to a wall or a stand. The turntable should be holding the vinyl record in a vertical position for better visibility of the album art.
- **Album Art Display**: The circular screen on the turntable displays the album art of the currently playing song on Spotify. The screen should be touch-enabled to allow for interaction with the music. The screen should be mounted to the middle of the vinyl record, mimicking the look of a real album. The album art should be displayed in a way that it looks like it is spinning when the music is playing.
- **User Interactions**: The user can interact with the turntable by touch gestures on the screen or by using the physical controls on the turntable.
    - **Touch Gestures**:
        - **Swipe**: Swiping left or right on the screen to skip to the next or previous song.
        - **Tap**: Tapping on the screen to pause or play the music.
        - **Rotate**: Rotating motion for adjusting the volume/track position.
    - **Physical Controls**:
        - **Tonearm Lifting**: Lifting the tonearm to pause or play the music.
        - **Volume Control**: Rotating a knob on the turntable to adjust the volume.
- **Integration with Spotify**: The turntable should be connected to the user's Spotify account to stream music directly from the service. The user can select playlists, albums, or songs to play on the turntable.
- **Customization Options**: The user can configure and customize the turntable's appearance, such as the color scheme, album art display settings, and more through a web interface.

## Hardware requirements
The Spotify Turntable requires the following hardware components to function properly (minimum requirements):

- **SBC (single board computer)**: The Raspberry Pi or similar is used as the brain of the turntable, handling the Spotify integration, touch screen display, and user interactions.
- **Touch Screen Display**: A circular touch screen display is used to show the album art and allow for user interactions.
- **Platter and Tonearm**: The physical components of the turntable, including the platter, tonearm, and vinyl record holder.

## Software requirements
The graphical application running on the Raspberry Pi utilizes the following software components:
- Spotify API: To connect to the Spotify service and stream music. [Spotipy](https://spotipy.readthedocs.io/) is a Python library that can be used to interact with the Spotify API.
- Web server: To host the web interface for customizing the turntable settings. [Flask](https://flask.palletsprojects.com/) is a lightweight web framework that can be used to create the web interface. The used platform might change in the future.
- Touch screen drivers: To enable touch interactions on the circular screen. The drivers depend on the specific touch screen model used.

## Project Status
The Spotify Turntable project is currently in the concept and design phase. The project aims to create a proof-of-concept prototype that demonstrates the functionality of the Spotify Turntable. The project is open to collaboration and contributions from the community.



