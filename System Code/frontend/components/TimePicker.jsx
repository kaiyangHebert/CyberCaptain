import { StyleSheet, Text, View, SectionList } from 'react-native'
import tw from 'tailwind-react-native-classnames'
import React, { useState } from 'react'
import { Button } from 'react-native-paper';
import { useStateContext } from '../context/ContextProvider'

const TimePicker = ({navigation}) => {
  const { scheduleTime, setScheduleTime, hour, setHour, minute, setMinute, handleClick } = useStateContext()

  const Item1 = ({ title }) => {
    if (title == hour) {
      return (
        <View style={tw`bg-gray-500 items-center`}>
          <Text style={tw`text-4xl`} onPress={() => { setHour(title) }}>{title}</Text>
        </View>
      )
    }
    else {
      return (
        <View style={tw`items-center`}>
          <Text style={tw`text-4xl`} onPress={() => { setHour(title) }}>{title}</Text>
        </View>
      )
    }
  };

  const Item2 = ({ title }) => {
    if (title == minute) {
      return (
        <View style={tw`bg-gray-500 items-center`}>
          <Text style={tw`text-4xl`} onPress={() => { setMinute(title) }}>{title}</Text>
        </View>
      )
    }
    else {
      return (
        <View style={tw`items-center`}>
          <Text style={tw`text-4xl`} onPress={() => { setMinute(title) }}>{title}</Text>
        </View>
      )
    }
  }

  const hoursData = [{
    data: ["00", "01", "02", "03", "04", "05", "06", "07",
      "08", "09", "10", "11", "12", "13", "14", "15",
      "16", "17", "18", "19", "20", "21", "22", "23"]
  }]
  const minutesData = [{
    data: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", 
    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", 
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
    "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", 
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", 
    "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", ]
  }]
  return (
    <>
      <View style={tw`justify-center items-center`} >
        <View style={tw`absolute bg-gray-300 w-5/6 h-60 pt-2 flex-row rounded-lg`}>
          <SectionList
            contentContainerStyle={tw``}
            sections={hoursData}
            keyExtractor={(item, index) => item + index}
            renderItem={({ item }) => <Item1 title={item} />}
            renderSectionHeader={({ section: { title } }) => (
              <Text style={styles.header}>{title}</Text>
            )}
          />
          <Text style={tw`text-4xl font-bold pt-20`}>:</Text>
          <SectionList
            contentContainerStyle={tw``}
            sections={minutesData}
            keyExtractor={(item, index) => item + index}
            renderItem={({ item }) => <Item2 title={item} />}
            renderSectionHeader={({ section: { title } }) => (
              <Text>{title}</Text>
            )}
          />
        </View>
      </View>
      <View style={tw`items-center`}>
      <View style={tw`absolute top-40`}>
        <Button 
        style={tw`bg-gray-300 pl-4 pr-4 pt-2 pb-2`} 
        onPress={() => {
          //setScheduleTime()
          let tempTime = new Date()
          tempTime.setHours(hour)
          tempTime.setMinutes(minute)
          setScheduleTime(tempTime);
          handleClick("");
          navigation.navigate("SetPickUp")
          }}>
        Confirm
        </Button>
        </View>
      </View>
    </>
  )
}

export default TimePicker

const styles = StyleSheet.create({})