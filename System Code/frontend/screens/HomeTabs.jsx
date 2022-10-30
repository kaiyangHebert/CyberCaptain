import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from './HomeScreen';
import ChatbotScreen from './ChatbotScreen';
import AccountScreen from './AccountScreen';
import Ionicons from 'react-native-vector-icons/Ionicons';

const Tab = createBottomTabNavigator();

const HomeTabs = ({navigation}) => {
  return (
    <>
      <Tab.Navigator
      screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === 'Home') {
              iconName = focused
                ? 'ios-home'
                : 'ios-home-outline';
            } else if (route.name === 'Chatbot') {
              iconName = focused ? 'md-chatbox-ellipses' : 'md-chatbox-ellipses-outline';
            }
            else if (route.name === 'Account') {
              iconName = focused ? 'ios-person' : 'ios-person-outline';
            }
            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: 'tomato',
          tabBarInactiveTintColor: 'gray',
          headerShown: false,
          tabBarStyle: {
            //padding:3,
          },
          tabBarItemStyle: {
            padding:5,
          }
        })}>
        <Tab.Screen name="Home" component={HomeScreen} navigation={navigation}/>
        <Tab.Screen name="Chatbot" component={ChatbotScreen} navigation={navigation}/>
        <Tab.Screen name="Account" component={AccountScreen} navigation={navigation}/>
      </Tab.Navigator>
    </>
  )
}

export default HomeTabs

