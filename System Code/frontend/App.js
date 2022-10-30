import { NavigationContainer } from '@react-navigation/native';
import { ContextProvider, useStateContext } from './context/ContextProvider';
import MainScreen from './screens/MainScreen';
//home 
export default function App() {
  return (
    <NavigationContainer>
    <ContextProvider>
    <MainScreen />
      </ContextProvider>
    </NavigationContainer>
  );
}

