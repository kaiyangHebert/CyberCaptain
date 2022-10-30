// In App.js in a new project
import { View } from 'react-native';
import React, { useState } from 'react';
import Carousel from '../components/Carousel'
import { TextInput, Button } from 'react-native-paper';
import tw from 'tailwind-react-native-classnames'
import Schedule from '../components/Schedule';
import { useStateContext } from '../context/ContextProvider'
import TimePicker from '../components/TimePicker';

const HomeScreen = ({ navigation }) => {
    const [place, setPlace] = useState(null);
    const { handleClick, isClicked} = useStateContext();
    return (
        <>
        <View style={tw`flex-col`}>
            <Carousel />
            <View style={tw`flex-row`}>
                <TextInput
                    style={tw`w-64`}
                    theme={{ roundness: 50 }}
                    mode='outlined'
                    label="Place"
                    placeholder='Where to?'
                    value={place}
                    editable={false}
                    onChangeText={place => setText(place)}
                    left={<TextInput.Icon icon="magnify" />}
                    onFocus={() => navigation.navigate("SetPickUp")}
                />
                <View style={tw`pt-1 pl-1`}>
                    <Button
                        style={tw`w-32 p-2`}
                        theme={{ roundness: 50 }}
                        icon="clock"
                        mode="contained"
                        contentStyle={{ flexDirection: 'row-reverse' }}
                        onPress={() => handleClick("schedule")}
                    >
                        Now
                    </Button>
                </View>
            </View>
        </View>
        {isClicked.schedule && <Schedule navigation={navigation}/>}
        {isClicked.setTime && <TimePicker navigation={navigation}/>}
        </>
    )
}

export default HomeScreen;