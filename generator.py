#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import os
import sys
import json
import argparse
from PIL import Image
from PIL import  ImageOps


def generate_icon_images_ios(icon_filename):
    sizes = [20, 29, 40, 60, 58, 76, 87, 120, 152, 180, 1024]
    image_name = icon_filename
    contents = {}
    content_template = {
        20: {
            "idiom": "ipad",
            "size": "20x20",
            "scale": "1x",
            "filename": "Icon-20x20@1x.png"
        },
        40: {
            "idiom": "iphone",
            "size": "20x20",
            "scale": "2x",
            "filename": "Icon-20x20@2x.png"
        },
        60: {
            "idiom": "iphone",
            "size": "20x20",
            "scale": "3x",
            "filename": "Icon-20x20@3x.png"
        },
        29: {
            "idiom": "iphone",
            "size": "29x29",
            "scale": "1x",
            "filename": "Icon-29x29@1x.png"
        },
        58: {
            "idiom": "iphone",
            "size": "29x29",
            "scale": "2x",
            "filename": "Icon-29x29@2x.png"
        },
        87: {
            "idiom": "iphone",
            "size": "29x29",
            "scale": "3x",
            "filename": "Icon-29x29@3x.png"
        },
        80: {
            "idiom": "iphone",
            "size": "40x40",
            "scale": "2x",
            "filename": "Icon-40x40@2x.png"
        },
        80: {
            "idiom": "iphone",
            "size": "40x40",
            "scale": "3x",
            "filename": "Icon-40x40@3x.png"
        },
        120: {
            "idiom": "iphone",
            "size": "60x60",
            "scale": "2x",
            "filename": "Icon-60x60@2x.png"
        },
        180: {
            "idiom": "iphone",
            "size": "60x60",
            "scale": "3x",
            "filename": "Icon-60x60@3x.png"
        },
        76: {
            "idiom": "ipad",
            "size": "76x76",
            "scale": "1x",
            "filename": "Icon-76x76@1x.png"
        },
        152: {
            "idiom": "ipad",
            "size": "76x76",
            "scale": "2x",
            "filename": "Icon-76x76@2x.png"
        },
        1024: {
            "idiom": "iphone",
            "size": "1024x1024",
            "scale": "1x",
            "filename": "Icon-marketing-1024x1024.png"
        },
        "info": {
            "version": 1,
            "author": "apsl"
        }
    }

    if os.path.isfile(image_name) is False:
        sys.exit("Missing {0} file".format(image_name))

    img = Image.open(image_name)

    # Check image size
    if img.size < (1024, 1024):
        sys.exit("{0} size is {1}. Must be 1024x1024 or higher.".format(image_name, img.size))

    # Create Assets folder
    current_dir = os.getcwd()
    asset_dir = "{0}/ios/AppIcon.appiconset".format(current_dir)
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    os.chdir(asset_dir)
    print asset_dir

    # Generate images
    images = []
    for size in sizes:
        i = img.resize((size, size), Image.ANTIALIAS)
        img_filename = content_template.get(size).get("filename")
        i.save(img_filename, format="PNG")
        images.append(content_template.get(size))
    contents["info"] = content_template["info"];
    contents["images"] = images
    file = open("Contents.json", "w")
    file.write(json.dumps(contents))
    file.close()
    os.chdir("../../")

def generate_icon_images_android(icon_filename):
    sizes = [{"size": 96, "folder":"drawable", "filename":"icon.png"},
             {"size": 72, "folder": "drawable-hdpi", "filename": "icon.png"},
             {"size": 36, "folder": "drawable-ldpi", "filename": "icon.png"},
             {"size": 48, "folder": "drawable-mdpi", "filename": "icon.png"},
             {"size": 96, "folder": "drawable-xhdpi", "filename": "icon.png"},
             {"size": 152, "folder": "drawable-xxhdpi", "filename": "icon.png"},
             {"size": 192, "folder": "drawable-xxxhdpi", "filename": "icon.png"}
             ]
    image_name = icon_filename
    contents = {}

    if os.path.isfile(image_name) is False:
        sys.exit("Missing {0} file".format(image_name))

    img = Image.open(image_name)

    # Check image size
    if img.size < (1024, 1024):
        sys.exit("{0} size is {1}. Must be 1024x1024 or higher.".format(image_name, img.size))

    # Create Assets folder
    current_dir = os.getcwd()
    asset_dir = "{0}/android".format(current_dir)
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    os.chdir(asset_dir)
    print asset_dir

    # Generate images
    for item in sizes:
        print item
        i = img.resize((item["size"], item["size"]), Image.ANTIALIAS)
        folder = "{0}/android/{1}".format(current_dir,item["folder"])
        if not os.path.exists(folder):
            os.makedirs(folder)
        img_filename = "{0}/android/{1}/{2}".format(current_dir,item["folder"],item["filename"])
        i.save(img_filename, format="PNG")
    os.chdir("../")


def generate_launch_image_ios(image_name):
    # 1334x750 not available yet, see: http://stackoverflow.com/a/26275887/1034126
    sizes = [{"size": [640,1136], "folder":"LaunchImage.launchimage", "filename":"LaunchImage-568h@2x~iphone_640x1136.png"},
             {"size": [1334,750], "folder": "LaunchImage.launchimage", "filename": "LaunchImage-750@2x~iphone6-landscape_1334x750.png"},
             {"size": [750,1334], "folder": "LaunchImage.launchimage", "filename": "LaunchImage-750@2x~iphone6-portrait_750x1334.png"},
             {"size": [2208, 1242], "folder": "LaunchImage.launchimage","filename": "LaunchImage-1242@3x~iphone6s-landscape_2208x1242.png"},
             {"size": [1242, 2208], "folder": "LaunchImage.launchimage", "filename": "LaunchImage-1242@3x~iphone6s-portrait_1242x2208.png"},
             {"size": [2048,1496], "folder": "LaunchImage.launchimage", "filename": "LaunchImage-Landscape@2x~ipad_2048x1496.png"},
             {"size": [2048, 1536], "folder": "LaunchImage.launchimage","filename": "LaunchImage-Landscape@2x~ipad_2048x1536.png"},
             {"size": [1024, 748], "folder": "LaunchImage.launchimage","filename": "LaunchImage-Landscape~ipad_1024x748.png"},
             {"size": [1024, 768], "folder": "LaunchImage.launchimage","filename": "LaunchImage-Landscape~ipad_1024x768.png"},
             {"size": [1536, 2008], "folder": "LaunchImage.launchimage","filename": "LaunchImage-Landscape~ipad_1536x2008.png"},
             {"size": [1536, 2048], "folder": "LaunchImage.launchimage","filename": "LaunchImage-Landscape~ipad_1536x2048.png"},
             {"size": [768, 1024], "folder": "LaunchImage.launchimage","filename": "LaunchImage-Portrait~ipad_768x1024.png"},
             {"size": [768, 1004], "folder": "LaunchImage.launchimage","filename": "LaunchImage.png"},
             {"size": [1536, 2008], "folder": "LaunchImage.launchimage","filename": "LaunchImage~ipad.png"},
             {"size": [640,960], "folder": "LaunchImage.launchimage", "filename": "LaunchImage~iphone_640x960.png"},
             {"size": [320, 480], "folder": "LaunchImage.launchimage", "filename": "LaunchImage~iphone-320x480.png"}
             ]


    if os.path.isfile(image_name) is False:
        sys.exit("Missing {0} file".format(image_name))

    img = Image.open(image_name)

    # Check image size
    if img.size < (2048,2048):
        sys.exit("{0} size is {1}. Must be 2048x2048.".format(image_name, img.size))

    # Create Assets folder
    current_dir = os.getcwd()
    asset_dir = "{0}/ios".format(current_dir)
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    os.chdir(asset_dir)
    print asset_dir

    # Generate images
    for item in sizes:
        img_size_x = item["size"][0]
        img_size_y = item["size"][1]
        print (2048-img_size_y) / 2
        print img_size_y
        #i = img.crop(((2048-img_size_x) / 2, (2048-img_size_y) /2, img_size_x + (2048-img_size_x) / 2, img_size_y + (2048-img_size_y) / 2))
        i = ImageOps.fit(img,(img_size_x, img_size_y), Image.NEAREST)
        folder = "{0}/ios/{1}".format(current_dir, item["folder"])
        if not os.path.exists(folder):
            os.makedirs(folder)

        img_filename = "{0}/{1}".format(folder,item["filename"])
        print img_filename
        i.save(img_filename, format="PNG")
    os.chdir("../")

def generate_launch_image_android(image_name):
    # 1334x750 not available yet, see: http://stackoverflow.com/a/26275887/1034126
    sizes = [{"size": [480, 800], "folder":"drawable", "filename":"splash.png"},
             {"size": [480, 800], "folder": "drawable-hdpi", "filename": "splash.png"},
             {"size": [800, 480], "folder": "drawable-land", "filename": "splash.png"},
             {"size": [800, 480], "folder": "drawable-land-hdpi", "filename": "splash.png"},
             {"size": [320, 200], "folder": "drawable-land-ldpi", "filename": "splash.png"},
             {"size": [480,320], "folder": "drawable-land-mdpi", "filename": "splash.png"},
             {"size": [1280, 720], "folder": "drawable-land-xhdpi", "filename": "splash.png"},
             {"size": [1600,960], "folder": "drawable-land-xxhdpi", "filename": "splash.png"},
             {"size": [1920, 1280], "folder": "drawable-land-xxxhdpi", "filename": "splash.png"},
             {"size": [200, 320], "folder": "drawable-ldpi", "filename": "splash.png"},
             {"size": [320,480], "folder": "drawable-mdpi", "filename": "splash.png"},
             {"size": [720, 1280], "folder": "drawable-xhdpi", "filename": "splash.png"},
             {"size": [960, 1600], "folder": "drawable-xxhdpi", "filename": "splash.png"},
             {"size": [1280, 1920], "folder": "drawable-xxxhdpi", "filename": "splash.png"},
             ]


    if os.path.isfile(image_name) is False:
        sys.exit("Missing {0} file".format(image_name))

    img = Image.open(image_name)

    # Check image size
    if img.size < (2048,2048):
        sys.exit("{0} size is {1}. Must be 2048x2048.".format(image_name, img.size))

    # Create Assets folder
    current_dir = os.getcwd()
    asset_dir = "{0}/android".format(current_dir)
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    os.chdir(asset_dir)
    print asset_dir

    # Generate images
    for item in sizes:
        img_size_x = item["size"][0]
        img_size_y = item["size"][1]
        print (2048-img_size_y) / 2
        print img_size_y
        #i = img.crop(((2048-img_size_x) / 2, (2048-img_size_y) /2, img_size_x + (2048-img_size_x) / 2, img_size_y + (2048-img_size_y) / 2))
        i = ImageOps.fit(img,(img_size_x, img_size_y))
        folder = "{0}/android/{1}".format(current_dir, item["folder"])
        if not os.path.exists(folder):
            os.makedirs(folder)

        img_filename = "{0}/{1}".format(folder,item["filename"])
        print img_filename
        i.save(img_filename, format="PNG")
    os.chdir("../")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Assets generator for iOS projects")
    parser.add_argument("--launchimage",
                        help="Generate launch image assets")
    parser.add_argument("--icon",
                        help="Generate icons assets")
    parser.parse_args()
    args = parser.parse_args()
    if args.launchimage:
        print "Generating launch image with image {0}".format(args.launchimage)
        generate_launch_image_ios(args.launchimage)
        generate_launch_image_android(args.launchimage)
    if args.icon:
        print "Generating icons with image {0}".format(args.icon)
        generate_icon_images_ios(args.icon)
        generate_icon_images_android(args.icon)
