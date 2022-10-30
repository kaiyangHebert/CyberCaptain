import { StyleSheet, Text, SafeAreaView, View, Image, ScrollView } from 'react-native'
import { TextInput, Button } from 'react-native-paper';
import tw from 'tailwind-react-native-classnames'
import React, { useState } from 'react'
import { useStateContext } from '../context/ContextProvider'
import { postData } from '../fetchMethod'
import { backendhost } from '../configure' 

const ChatbotScreen = () => {
  const [context, setContext] = useState('')
  const [tag1, setTag1] = useState(false)
  const [tag2, setTag2] = useState(true)
  const [tag3, setTag3] = useState(false)
  const [tag4, setTag4] = useState(false)
  const { chats, setChats, profile } = useStateContext()
  const handleClick = () => {
    setChats([...chats, {
      name: 'user',
      text: context
    }])
    console.log(chats)
    postData(backendhost+'chatbot', { context: context, tag1: tag1, tag2: tag2, tag3: tag3, tag4: tag4,name: profile.name })
      .then((data) => {
        console.log(typeof (data))
        console.log(data)
        setChats([...chats, {
          name: 'user',
          text: context
        },{
          name: 'bot',
          text: data[0],
        }])
        setTag1(data[1])
        setTag2(data[2])
        setTag3(data[3])
        setTag4(data[4])
      })
      setContext('')
  }
  return (
    <>
      <SafeAreaView style={tw`top-8 pb-32`}>
        <ScrollView>
          {chats.map((chat, index) => {
            return (
              <View style={tw`flex p-2 flex-row`} key={`${chat.text}-${index}`}>
                {chat.name === 'bot' &&
                  <><Image style={tw`w-8 h-8 p-1`} source={require('../assets/bot.png')} /><Text style={tw`bg-gray-200 p-2 rounded-lg text-lg w-80`}>
                    {chat.text}
                  </Text></>}
                {chat.name === 'user' &&
                  <><Text style={tw`bg-yellow-400 p-2 rounded-lg ml-auto text-xl italic`}>
                    {chat.text}
                  </Text>
                    <Image style={tw`w-8 h-8 p-1`} source={require('../assets/avatar.png')} /></>}
              </View>
            )
          }
          )}
        </ScrollView>
      </SafeAreaView>

      <View style={tw`absolute bottom-0`}>
        <View style={tw`flex-row`}>
          <TextInput
            style={tw`w-64`}
            theme={{ roundness: 50 }}
            mode='outlined'
            onChangeText={text => setContext(text)}
            value={context}
          //onFocus={() => navigation.navigate("SetPickUp")}
          />
          <View style={tw`pt-1 pl-1`}>
            <Button
              style={tw`w-32 p-2`}
              theme={{ roundness: 50 }}
              mode="contained"
              onPress={() => handleClick()}
            >
              Send
            </Button>
          </View>
        </View>
      </View>
    </>
  )
}



export default ChatbotScreen
