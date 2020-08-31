# dam-sync

![dam-sync](https://s3-eu-west-1.amazonaws.com/public-stuff-cdn/suitcase.jpg)

DAM-Sync is a small console utility that will help you keep your digital assets
library backed up to multiple locations: external connected storage and the 
AWS S3. 

It uses an incremental approach so only the files that have changed will be moved. For this it uses two utilities that you need to install (see below).

As off-site cloud storage is expensive it's recommended to configure your AWS S3 bucket storage to use Glacier or GlacierDeepArchive storag type with the latter being very cost-effective. You might, however, consider other storage types if you need more frequent access to your cloud since Glacier is an infrequent access storage (hence the low price).

## Release notes

  * [Release notes and Changelog](docs/changelog.md)


## Basic usage

After it's installed and configured (see below) it's quite straightforward to use. Backup your library to both attached storage and cloud by running:

```
dam-sync run
```

Or you can choose to backup to attached storage only with the `--disk` flag:

```
dam-sync run --disk
```

Or only to cloud with the `--cloud` flag:

```
dam-sync run --cloud
```


## Installation

This library requires Python3 to run and is ideal when installed globally. Install it with pip:

```
pip install dam-sync
```

As it is meant to be installed globally, it has intentionally limited dependencies and doesn not bundle tools that can interfere with packages/versions installed on your system. Instead, it relies on those packages being present on your system.

Basically there are only two dependencies: `rsync` and `aws-cli`. Install them both before using this tool. the best way to get them is from [Homebrew](https://brew.sh/)

#### Install rsync

First check if you have it already, as it might come with your system or other tools:

```
rsync --version
```

If you don't, then go ahead and grab it from brew:


```
brew install rsync

```

#### Install awscli

Same thing goes for `awscli` check if you have it already:

```
aws --version
```

And install it if not:

```
brew install awscli
```

When first installed, you will need to confgure it with access credentials you obtained from AWS:

```
aws configure
```

#### Limited AWS access

If you wish, you can use a limited privileges AWS profile that only has access to the specific bucket you will back up to. If that's the case, create a new IAM user in AWS and assign proper permissions. You can then edit your `./aws/credentials` file to add a new profile with those IAM user credentials:

```
[dam_sync]
aws_access_key_id = KEY-HERE
aws_secret_access_key = longer-secret-here
```

You can then tell `dam-sync` to use this profile for backups.

