import { StyleSheet, Text, View, Image } from 'react-native'
import tw from 'tailwind-react-native-classnames'
import shareVideo from '../data/share.mp4';
import React, { useState } from 'react'
import { TextInput, Button } from 'react-native-paper';
import { useStateContext } from '../context/ContextProvider'
import { postData } from '../fetchMethod'
import { backendhost } from '../configure' 
import Axios from 'axios';

const Register = ({ navigation }) => {
    const [name, setName] = useState('');
    const [password, setPassword] = useState('');
    const [correct, setCorrect] = useState(true);
    const [accountExist,setAccountExist] = useState(false);
    const [destination, setDestination] = useState('');
    const { setLogin, setprofile } = useStateContext();

    //const handleClick = () => {
    //    Axios.post("http://localhost:3001/register", {
    //  name: name,
    //  password: password,
    //  destination: destination
    //}).then(() => {
    //    setLogin(true)
    //    setprofile({
    //        name: name,
    //        destination: destination
    //    })
    //});


    const handleClick = () => {
        postData(backendhost+'register', { name: name, password: password, destination: destination })
            .then((data) => {
                console.log(data);
                console.log(typeof (data));
                if(data){
                    setLogin(true)
                    setprofile({
                        name: name,
                        destination: destination
                    })
                    navigation.navigate("HomeTabs")
                }
                else {
                    setAccountExist(true)
                }
                //if (data.length != 0) {
                //    setLogin(true)
                //    setprofile({
                //        name: data[0][0],
                //        destination: data[0][1]
                //    })
                //}
            }
        );
    }
    return (
        <View style={tw`flex justify-start items-center flex-col w-full h-full`}>
            <View style={tw`relative w-full h-full`}>
            <Image 
      style={tw`h-full w-full`}
      source={require('../assets/background.jpg')}
      />
                <View style={tw`absolute flex flex-col justify-center items-center top-0 right-0 left-0 bottom-0`}>
                <Image style={tw`w-64 h-16`} source={require('../assets/logo.png')}/>
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
                    {correct && <View style={tw`pt-1`}></View>}
                    {!correct && <View><Text style={tw`text-red-600 text-xs`}>password is incorrect</Text></View>}
                    <TextInput
                        style={tw`w-64`}
                        theme={{ roundness: 50 }}
                        mode='outlined'
                        label="confirm password"
                        secureTextEntry={true}
                        onChangeText={text => { if (text == password) { setCorrect(true) } else { setCorrect(false) } }}
                        left={<TextInput.Icon icon="lock" />}
                    />
                    {correct && <View style={tw`pt-1`}></View>}
                    {!correct && <View><Text style={tw`text-red-600 text-xs`}>password is incorrect</Text></View>}
                    <View style={tw`pt-1`}></View>
                    <TextInput
                        style={tw`w-64`}
                        theme={{ roundness: 50 }}
                        mode='outlined'
                        label="prefer destination"
                        onChangeText={text => setDestination(text)}
                        left={<TextInput.Icon icon="google-maps" />}
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
                            Register
                        </Button>
                    </View>
                    {accountExist && <View><Text style={tw`text-red-600 text-sm font-bold`}>account has existed</Text></View>}
                </View>
            </View>
        </View>
    )
}

export default Register

const styles = StyleSheet.create({
    video: {
        width: '100%',
        height: '100%',
        resizeMode: 'cover'
    }
})