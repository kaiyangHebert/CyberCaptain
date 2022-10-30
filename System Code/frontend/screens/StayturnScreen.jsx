import { View,Image,Text } from 'react-native'
import React from 'react'

import stayTurned from '../assets/stay-turned.jpg'
import tw from 'tailwind-react-native-classnames'

const StayturnScreen = () => {
  return (
    <View style={tw`h-full w-full`}>
      <Image 
      style={tw`h-full w-full`}
      source={require('../assets/stay-turned.jpg')}
      />
    </View>
  )
}

export default StayturnScreen