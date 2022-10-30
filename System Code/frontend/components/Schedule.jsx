import { Text, View } from 'react-native'
import React, { useState } from 'react'
import { List } from 'react-native-paper';
import tw from 'tailwind-react-native-classnames'
import { useStateContext } from '../context/ContextProvider';
//import { }

const Schedule = ({navigation}) => {
  const { scheduleTime, setScheduleTime, handleClick } = useStateContext()
  const getPeriod = (time) => {
    let minutes = Math.floor(scheduleTime.getMinutes() / 10) * 10;
    return [minutes, minutes + 10]
  }
  return (
    <View style={tw`w-11/12 h-60 bg-gray-300 bottom-0 rounded-lg absolute right-5`}>
      <List.Section>
        <List.Subheader style={tw`items-center text-center font-bold text-lg`}>Schedule a Ride</List.Subheader>
        <List.Item
          title={scheduleTime.toUTCString().slice(0, 11)}
          style={tw`items-center`}
        />
        <List.Item
          title={`${scheduleTime.getHours()} : ${getPeriod(scheduleTime)[0]} - ${scheduleTime.getHours()} : ${getPeriod(scheduleTime)[1]}`}
          style={tw`items-center`}
          onPress={() => { handleClick("setTime") }}
        />
        <List.Item
          title={`Set pickup time`}
          titleStyle={tw`text-white`}
          style={tw`items-center bg-black`}
          onPress={() => navigation.navigate("SetPickUp")}
        />
      </List.Section>
    </View>
  )
}

export default Schedule