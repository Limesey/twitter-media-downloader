# Twitter Video Downloader

Twitter Video Downloader allows you to download videos from multiple tweets.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Features](#features)
- [Technologies](#technologies)

## Introduction

Twitter Video Downloader web scrapes Twitter in order to find videos.
It then uses youtube-dl to download them.

## Setup

Clone this repository using Git:

```
$ git clone git@github.com:Limesey/twitter-media-downloader.git
```

Install the project's dependencies:

```
$ pip install -r requirements.txt
```

Run:

```
$ python src/cli.py
```

## Features

- Download Twitter videos
- Makes it easy to download your bookmarked videos

## Technologies

- [Python 3.8.4](https://www.python.org/)
- [argparse 1.4.0](https://pypi.org/project/argparse/)
- [Selenium 3.141.0](https://pythonspot.com/selenium/)
- [python-dotenv 0.17.0](https://pypi.org/project/python-dotenv/)
- [youtube_dl 2021.4.7](https://pypi.org/project/youtube_dl/)

## Sources

- This README was created following [bulldogjob.com](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)'s guide.