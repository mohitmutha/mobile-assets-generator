# mobile-assets-generator
Python script to generate icon image and launch image assets for the iOS and Android. 

## Requirements ##
- Python should be installed
- Pillow should be installed [[https://pillow.readthedocs.io/en/latest/]]
- Icon image of 1024 x 1024
- Launch image of 2048 x 2048

### Usage ###
From command line run 

```
./generator.py --launchimage <LAUNCHIMAGE_PATH> --icon <ICONIMAGE_PATH>
```

For the launch image ensure that the content is placed in the center with space around it. The script trims around the center to produce images of different sizes.
