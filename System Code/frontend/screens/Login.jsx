import { StyleSheet, Text, View, Image } from 'react-native'
import tw from 'tailwind-react-native-classnames'
import shareVideo from '../data/share.mp4';
import image from '../assets/1.jpg'
import React, { useState } from 'react'
import { TextInput, Button } from 'react-native-paper';
import { useStateContext } from '../context/ContextProvider'
import { postData } from '../fetchMethod'
import { backendhost } from '../configure' 
import Axios from 'axios';

const Login = ({ navigation }) => {
    const [name, setName] = useState();
    const [password, setPassword] = useState('');
    const [incorrect, setIncorrent] = useState(false);
    const { setLogin, setprofile } = useStateContext();

    //const handleClick = () => {
    //    Axios.put("http://localhost:3001/uberdata", { name: name, password: password }).then((respose) => {
    //        if (respose!= null) {
    //            setLogin(true)
    //            setprofile(respose);
    //        }
    //    })
    //    setIncorrent(true);
    //}
    const handleClick = () => {
        postData(backendhost+'login', { name: name, password: password })
            .then((data) => {
                console.log(data);
                if (data.length != 0) {
                    setLogin(true)
                    setprofile({
                        name: data[0][0],
                        destination: data[0][1]
                    })
                }
                else{
                    setIncorrent(true)
                }
            }
        );
    }
    //Axios.post("http://localhost:5000", { name: name, password: password }).then((respose) => {
    //fetch("http://localhost:5000").then(
    //    res => res.json()
    //).then(
    //    data => {
    //        console.log(data)
    //    }
    //)
    return (
        <View style={tw`flex justify-start items-center flex-col w-full h-full`}>
            <View style={tw`relative w-full h-full`}>
            <Image 
      style={tw`h-full w-full`}
      source={require('../assets/background.jpg')}
      />
                <View style={tw`absolute flex flex-col justify-center items-center top-0 right-0 left-0 bottom-0`}>
                    <Image style={tw`w-64 h-16`} source={require('../assets/logo.png')}/>
                    <View style={tw`pt-1`}></View>
                    <TextInput
                        style={tw`w-64`}
                        theme={{ roundness: 50 }}
                        mode='outlined'
                        label="username"
                        onChangeText={text => setName(text)}
                        left={<TextInput.Icon icon="account" />}
                    />
                    <View style={tw`pt-1`}></View>
                    <TextInput
                        style={tw`w-64`}
                        theme={{ roundness: 50 }}
                        mode='outlined'
                        label="password"
                        secureTextEntry={true}
                        onChangeText={text => setPassword(text)}
                        left={<TextInput.Icon icon="lock" />}
                    />
                    <View style={tw`pt-1`}></View>
                    <View style={tw`flex-row`}>
                        <Button
                            style={tw`w-28 p-1`}
                            theme={{ roundness: 50 }}
                            mode="contained"
                            contentStyle={{ flexDirection: 'row-reverse' }}
                            onPress={() => handleClick()}
                        >
                            Login
                        </Button>
                        <View style={tw`pl-4`}></View>
                        <Button
                            style={tw`w-28 p-1`}
                            theme={{ roundness: 50 }}
                            mode="contained"
                            contentStyle={{ flexDirection: 'row-reverse' }}
                            onPress={() => { navigation.navigate("Register") }}
                        >
                            Register
                        </Button>
                    </View>
                    {incorrect && <Text style={tw`text-red-700 text-xl`}>Incorrect username or password.</Text>}
                </View>
            </View>
        </View>
    )
}

export default Login

const styles = StyleSheet.create({
    video: {
        width: '100%',
        height: '100%',
        resizeMode: 'cover'
    }
})