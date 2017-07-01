/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Image
} from 'react-native';
import Izzati from 'react-native-izzati';
import ImagePicker from 'react-native-image-picker';
import ImageResizer from 'react-native-image-resizer';

let options = {
    title: 'Select Image',
    customButtons: [
        {name: 'fb', title: 'Choose Photo from Facebook'},
    ],
    storageOptions: {
        skipBackup: true,
        path: 'images'
    }
};

export default class IzzatiTest extends Component {
  constructor(props) {
      super(props);
      this.state = {uri: "http://lorempixel.com/200/400/sports/5/"}
      ImagePicker.showImagePicker(options, (response) => {
        if (response.didCancel) {
          console.log('User cancelled image picker');
        }
        else if (response.error) {
          console.log('ImagePicker Error: ', response.error);
        }
        else if (response.customButton) {
          console.log('User tapped custom button: ', response.customButton);
        }
        else {
          base64data = response.data;
          datauri = 'data:image/jpeg;base64,' + base64data
          ImageResizer.createResizedImage(datauri, 640, 480, 'JPEG', 80).then((resizedImageUri) => {
              let i = new Izzati("http://192.168.1.17:5020/")
              i.send({text: {hello: 'me'}, file: {uri: resizedImageUri, filename: 'photo.jpg'}, response: {base64: false}}, (out) => {
                  this.setState(previous => {
                      return {uri: i.prefixPath(out.path)}
                })
              })
          }).catch((err) => {
              console.log(err)
          })
          }
      });
  }
  render() {
    return (
      <View style={styles.container}>
        <Image style={{flex: 1}} source={{uri: this.state.uri}} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'stretch'
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});

AppRegistry.registerComponent('IzzatiTest', () => IzzatiTest);
