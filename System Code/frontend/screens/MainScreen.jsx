import { StyleSheet, Text, View } from 'react-native'
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { useStateContext } from '../context/ContextProvider'
import HomeTabs from './HomeTabs'
import SetPickUp from './SetPickUp'
import Login from './Login'
import React from 'react'
import Register from './Register';


const MainScreen = () => {
  const Stack = createNativeStackNavigator();
  const { login } = useStateContext();
  return (
    <Stack.Navigator
    screenOptions = {({route}) => ({
      headerShown: false,
    })}
    >
      {!login && <Stack.Screen name="Login" component={Login} />}
      <Stack.Screen name="HomeTabs" component={HomeTabs} />
      <Stack.Screen name="SetPickUp" component={SetPickUp} />
      <Stack.Screen name="Register" component={Register} />
    </Stack.Navigator>
  )
}

export default MainScreen

const styles = StyleSheet.create({})