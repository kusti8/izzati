Quickstart - React Native
==============================

Install
------------

.. code-block:: bash

    npm i react-native-izzati --save
    RNFB_ANDROID_PERMISSIONS=true react-native link react-native-fetch-blob

Usage
-----------

1. Import it ``import Izzati from 'react-native-izzati'``

2. Then create a new instance with the URL ``let i = new Izzati("http://192.168.1.17:5020/")``

3. Then send, using ``i.send(options)``. The format is described in the
below table.

**The input options object has three items which are all themselves objects, text, file, and response.**
Not all of them must be used. All are optional.

+-------+----------+----------+----------------------------------------------------------------------------------------+
| text  | file     | response | notes                                                                                  |
+=======+==========+==========+========================================================================================+
| key   |          |          | The dict key                                                                           |
+-------+----------+----------+----------------------------------------------------------------------------------------+
| value |          |          | The dict value                                                                         |
+-------+----------+----------+----------------------------------------------------------------------------------------+
|       | uri      |          | A path                                                                                 |
+-------+----------+----------+----------------------------------------------------------------------------------------+
|       | base64   |          | A base64 representation of the data, **without** proper data:image/jpeg;base64, prefix |
+-------+----------+----------+----------------------------------------------------------------------------------------+
|       | filename |          | The filename of the file                                                               |
+-------+----------+----------+----------------------------------------------------------------------------------------+
|       |          | base64   | true or false. If false, then a path is outputted                                      |
+-------+----------+----------+----------------------------------------------------------------------------------------+

An example would be ``{text: {hello: 'me'}, file: {uri: resizedImageUri, filename: 'photo.jpg'}, response: {base64: false}}``

**The output object has three possible outputs, text, base64, or path.**

+--------+------------------------------------------------------------------------+
| text   | This is a normal JS object, when text is returned.                     |
+--------+------------------------------------------------------------------------+
| base64 | This is the base64 representation of a file, without the prefix.       |
+--------+------------------------------------------------------------------------+
| path   | This is the path of the file, without the required file:// on Android. |
+--------+------------------------------------------------------------------------+

The callback only takes one argument, and that is the out object.

A few functions exist other than send.

**prefixJpg(base64)**

Adds 'data:image/jpeg;base64,' to base64 and returns the result.

**prefixPath(path)**

Adds 'file://' if on Android and returns the result.

Example
-----------

.. code-block:: javascript

    let i = new Izzati("http://192.168.1.17:5020/")
    i.send({text: {hello: 'me'}, file: {uri: resizedImageUri, filename: 'photo.jpg'}, response: {base64: false}}).then( out => {
        this.setState(previous => {
            return {uri: i.prefixPath(out.path)}
      })
    }).catch(err => {
        console.log(err)
    })
    ...
    <Image style={{flex: 1}} source={{uri: this.state.uri}} />
