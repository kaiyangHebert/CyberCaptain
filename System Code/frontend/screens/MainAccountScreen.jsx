import { View, Image, Text,SafeAreaView } from 'react-native'
import { Button, List } from 'react-native-paper';
import tw from 'tailwind-react-native-classnames'
import React from 'react'
import { useStateContext } from '../context/ContextProvider'

const MainAccountScreen = ({ navigation }) => {
    const { profile } = useStateContext()
    return (
        <SafeAreaView style={tw`flex p-4 justify-between top-8`}>
            <View style={tw`flex-row justify-between`}>
                <View style={tw`pt-6 pl-2`}>
                    <Text style={tw`text-xl font-black`}>{profile.name}</Text>
                </View>
                <Image
                    style={tw`rounded-full w-20 h-20`}
                    source={require('../assets/avatar.png')}
                    //source={require(profile[0].image)}
                >
                </Image>
            </View>
            <View style={tw`flex-row pt-10`}>
                <View style={tw`text-xl left-4`}>
                    <Button
                        style={tw`w-32 flex-row`}
                        labelStyle={{ fontSize: 35,color: '#000' }}
                        icon="help-circle"
                        onPress={() => navigation.navigate('StayturnScreen')}
                    />
                    <Text style={tw`pl-4`}>Help</Text>
                </View>
                <View style={tw`text-xl left-4`}>
                    <Button
                        style={tw`w-32 flex-row`}
                        labelStyle={{ fontSize: 35,color: '#000' }}
                        icon="wallet-outline"
                        onPress={() => navigation.navigate('StayturnScreen')}
                    />
                    <Text style={tw`pl-4`}>Wallet</Text>
                </View>
                <View style={tw`text-xl left-4`}>
                    <Button
                        style={tw`w-32 flex-row`}
                        labelStyle={{ fontSize: 35,color: '#000' }}
                        icon="clock"
                        onPress={() => navigation.navigate('StayturnScreen')}
                    />
                    <Text style={tw`pl-4`}>Trips</Text>
                </View>
            </View>
            <View style={tw`w-full pt-8`}>
                <List.Section>
                    <List.Item title="Messages" left={() => <List.Icon icon="email-newsletter"/>} onPress={() => navigation.navigate('StayturnScreen')}/>
                    <List.Item title="Settings" left={() => <List.Icon icon="account-settings"/>} onPress={() => navigation.navigate('StayturnScreen')}/>
                    <List.Item title="Legal" left={() => <List.Icon icon="information"/>} onPress={() => navigation.navigate('StayturnScreen')}/>
                </List.Section>
            </View>
        </SafeAreaView>
    )
}

export default MainAccountScreen;
{/*<Button onPress={() => navigation.navigate('StayturnScreen')} title="Button">Button</Button>*/ }