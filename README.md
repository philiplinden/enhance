# enhance
Image stitching and multi-frame super-resolution from video

## Install
requirements
- Python>=3.6
- Click
- OpenCV>=4.0.0

## Run
1. make the CLI executible `chmod +x ./enhance`
2. `./enhance --help`

## Quickstart
Clone this repo.
```bash
git clone git@github.com:philiplinden/enhance.git
```

Download sample images and save them to `.../enhance/images`.
```bash
git clone git@github.com:opencv/opencv_extra.git
cp opencv_extra/testdata/stitching enhance/images
cd enhance/images
```

Make sure the CLI entry point has executable permissions.
```bash
chmod +x ./enhance
```

Then run the CLI and have some fun.
```bash
# whats what
./enhance --help

# lets try stitching 
./enhance stitch --help

# ok but for real
./enhance stitch images/boat

# loud mode
./enhance -v stitch images/boat

# cacophony mode
./enhance --debug stitch images/boat
