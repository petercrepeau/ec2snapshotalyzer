# ec2shapshotalyzer

Demo project to mange AWS EC2  instance snapshots

## About

This project is a demo, and users boto3 to manage EC2 instance snapshots.

## Configuring

Shotty users the configuration file create by the AWS cli e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* for instances are list, start, or stop, for volumes is list, and snapshots is list
*project* is optional
