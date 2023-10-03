import React, {useState} from "react";
import {Text, View, StyleSheet, Image, TouchableOpacity} from 'react-native'
import * as ImagePicker from 'expo-image-picker'
import image from './assets/iselin.jpeg'

const App = () => {

  const [selectedImage, setSelectedImage] = useState(null)
  
  let openImagePickerAsync = async () => {
    let permissionResult = await ImagePicker.requestMediaLibraryPermissionsAsync()
  
    if (permissionResult.granted === false) {
      alert('Image permissions to access is required');
      return;
    }

    const pickerResult = await ImagePicker.launchImageLibraryAsync()
    if (pickerResult.canceled === true) {
      return;
    }

    setSelectedImage({localUri: pickerResult.uri});
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Ticket Bus</Text>
      <Image
        source={selectedImage !== null ? selectedImage.localUri: image}
        style={styles.image}
        />  
      <TouchableOpacity
        onPress={openImagePickerAsync}
        style={styles.button}
      >
      <TouchableOpacity
        onPress={openImagePickerAsync}
        style={styles.button2}
      ></TouchableOpacity>
        <Text style={styles.buttonText}>Elige una imagen</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { 

  flex: 1, justifyContent: "center", alignItems: "center", backgroundColor: "orange"},
  title: { fontSize:30, color: "black", fontWeight: "bold"},
  image: {height: 300, width:400, borderBlockColor: "black", borderRadius: 200},
  button: { backgroundColor: "red", border: "1px solid", padding: 12, marginTop: 10},
  buttonText: { fontSize: 22, color: "white"}

})

export default App