import { TextInput } from "react-native";
import React, {useState} from 'react'
import tw from 'tailwind-react-native-classnames'


export default function Search() {
    const [place,setPlace] = useState(null);
  return (

      <TextInput
        style={tw`h-10 m-3 p-2 border-2 rounded-full`}
        //style={styles.input}
        onChangeText={setPlace}
        value={place}
        placeholder="Where to?"
        />
  )
}
