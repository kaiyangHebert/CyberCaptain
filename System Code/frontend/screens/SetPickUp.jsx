import { StyleSheet, View, SafeAreaView, Image, Text } from 'react-native'
import { TextInput, Button } from 'react-native-paper';
import tw from 'tailwind-react-native-classnames'
import { useStateContext } from '../context/ContextProvider'
import React, { useState, useEffect } from 'react'
import { postData } from '../fetchMethod'
import { backendhost } from '../configure' 
import Axios from 'axios';

const SetPickUp = ({ navigation }) => {
  const { profile, scheduleTime, hour, minute } = useStateContext();
  const [destination, setDestination] = useState('');
  const [showImage, setShowImage ] = useState(false)
  const [imagesrc, setImagesrc] = useState('')
  const [str, setStr] = useState('')
  // const handleClick = () => {
  //   console.log(destination)
  //   postData(backendhost+'map', { destination: destination})
  //   .then((image) => {
  //       console.log(image)
  //       // setImagesrc(image.imgUrl)
  //       //console.log(typeof(imagesrc))

  //   })
  //   setShowImage(true)
  //   console.log(showImage)
  //   console.log(imagesrc)
  // }

  const handleClick = () => {

    Axios.post(backendhost+'map', { destination:destination == ''?profile.destination:destination, hour:hour, minute:minute }).then((respose) => {
      // console.log(respose)
      // setTimeout(()=>{setImagesrc(respose.data[0])},10000)
      setImagesrc(respose.data[0])
      setStr(respose.data[1])
      setShowImage(true)
      // setTimeout(()=>{setShowImage(true)},10000)
  })
  }
  //useEffect(() => {setPlace(profile.destination)},[])
  console.log(scheduleTime)
  return (
    <SafeAreaView style={tw`top-8`}>
      <TextInput
        style={tw`w-full`}
        theme={{ roundness: 50 }}
        mode='outlined'
        label="Start Place"
        placeholder='Where to?'
        value="University Town, NUS"
        editable={false}
        left={<TextInput.Icon icon="magnify" />}
      //onFocus={() => navigation.navigate("SetPickUp")}
      />
      <View style={tw`pt-1`}></View>
      <TextInput
        style={tw`w-full`}
        theme={{ roundness: 50 }}
        mode='outlined'
        label="Go To Pin"
        placeholder={profile.destination}
        onChangeText={text => setDestination(text)}
        left={<TextInput.Icon icon="magnify" />}
      //onFocus={() => navigation.navigate("SetPickUp")}
      />
      <View style={tw`p-1`}></View>
      <Button
        style={tw`w-32 p-2`}
        theme={{ roundness: 50 }}
        mode="contained"
        onPress={() => handleClick()}
      >
        Confirm
      </Button>
      {/* {showImage && setTimeout(()=>(<>
      <Image style={tw`w-full h-40 p-1`} source={`data:image/png;base64, ${imagesrc}`}></Image>
      <Text style={tw`text-xl italic p-1`}>{str}</Text>
      </>),3000)} */}
            {showImage && <>
      <View style={tw`p-2`}></View>
      <Image style={tw`w-full h-40 p-1`} source={{uri:`data:image/png;base64, ${imagesrc}`}}></Image>
      <Text style={tw`text-xl p-1`}>{str}</Text>
      </>}
    </SafeAreaView>
  )
}

export default SetPickUp

const styles = StyleSheet.create({})