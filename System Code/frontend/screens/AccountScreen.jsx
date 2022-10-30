import React from 'react'
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import StayturnScreen from './StayturnScreen'
import MainAccountScreen from './MainAccountScreen'

const Stack = createNativeStackNavigator();

const AccountScreen = () => {
  return (
    <Stack.Navigator
      screenOptions={({ route }) => ({
        headerShown: false,
      })}
    >
      <Stack.Screen name="MainAccountScreen" component={MainAccountScreen} />
      <Stack.Screen name="StayturnScreen" component={StayturnScreen} />
    </Stack.Navigator>
  )
}

export default AccountScreen