# ZooKeeper Dashboard

**Author: [Patrick Hunt](http://people.apache.org/~phunt/)** (follow me on [twitter](http://twitter.com/phunt))

## Summary

[This project](http://github.com/phunt/zookeeper_dashboard) uses Django and [kazoo](https://github.com/python-zk/kazoo) to provide a dashboard for a ZooKeeper ensemble (cluster).

*   Cluster summary
*   Individual server detail
*   Client connection detail
*   Navigate &amp; examine the live znode hierarchy

This is a work in progress. Want more? Ping me on [twitter](http://twitter.com/phunt) or enter an [issue](http://github.com/phunt/zookeeper_dashboard/issues) on GitHub.

### What's Apache ZooKeeper?

From the [official site](http://hadoop.apache.org/zookeeper/): "ZooKeeper is a high-performance coordination service for distributed applications."

It exposes common services - such as naming, configuration management, synchronization, and group services - in a simple interface so you don't have to write them from scratch. You can use it off-the-shelf to implement consensus, group management, leader election, and presence protocols.

## Overview

Django and the [kazoo](https://github.com/python-zk/kazoo) are used to provide a dashboard for a ZooKeeper ensemble (cluster).

## License

This project is licensed under the Apache License Version 2.0

## Requirements

*   Django 1.5+
*   kazoo 1.1+

## Usage

Edit settings.xml. The top of the file has the ZOOKEEPER specific settings.

*   ZOOKEEPER_SERVERS - host:port(,host:port)* of all servers in your cluster. This is the same information that you provide in your ZooKeeper client configuration.

Virtualenv is the easiest way to run the code. Create a local virtualenv directory and install the required packages

        virtualenv venv
        . venv/bin/activate
        pip install -r requirements.txt
        deactivate

then start the django server

        . venv/bin/activate
        ./manage.py runserver
        deactivate

Obviously the dashboard needs access to the serving cluster (it queries the server's client port per ZOOKEEPER_SERVERS configuration).

Finally open a link in your browser to the server: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

ZooKeeper client output is written to "cli_log.txt".

## Limitations

ACLs are not yet fully supported. In particular the django server runs as an un-authenticated user. If nodes are protected by ACLs the server will not be able to access them.

## Screenshots

### Cluster Summary

[![dashboard_summary](http://farm3.static.flickr.com/2483/4035924997_f97e4901ef.jpg)](http://www.flickr.com/photos/35605239@N00/4035924997/ "dashboard_summary by phunt, on Flickr")

### Server Summary

[![dashboard_server_summary](http://farm3.static.flickr.com/2630/4035924977_a18d7639f1.jpg)](http://www.flickr.com/photos/35605239@N00/4035924977/ "dashboard_server_summary by phunt, on Flickr")

### ZNode tree

ACLs and child list not shown

[![dashboard_tree_znode](http://farm3.static.flickr.com/2495/4036673608_495c4594ef.jpg)](http://www.flickr.com/photos/35605239@N00/4036673608/ "dashboard_tree_znode by phunt, on Flickr")
