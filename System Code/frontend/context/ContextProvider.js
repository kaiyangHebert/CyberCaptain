import React, { createContext, useContext, useState, useEffect } from 'react';
import { userProfile } from '../data/userProfile'


const initialState = {
    schedule: false,
    setTime:false,
}
const StateContext = createContext();



export const ContextProvider = ({ children }) => {
    const [isClicked, setIsClicked] = useState(initialState);
    const [scheduleTime, setScheduleTime] = useState(new Date());
    const [profile, setprofile] = useState(userProfile);
    const [login, setLogin] = useState(false);
    const [hour, setHour] = useState(new Date().getHours())
    const [minute, setMinute] = useState(new Date().getMinutes())
    const [chats, setChats] = useState([
        //{
        //  name: 'bot',
        //  text: "please input your drop-off location"
        //},
        {
            name: 'bot',
            text: "Hello, my name is Captain chatbot."
          },
        {
            name: 'bot',
            text: `Welcome ${profile.name}, I get your default drop-off address ${profile.destination}. Do you want to change it? (Please input yes or no)`
        },
      ]);

      useEffect(()=>{setChats(
        [{
            name: 'bot',
            text: "Hello, my name is Captain chatbot."
          },
        {
            name: 'bot',
            text: `Welcome ${profile.name}, I get your default drop-off address ${profile.destination}. Do you want to change it? (Please input yes or no)`
        }],
      )},[profile])
    //const [profile, setprofile] = useState(userProfile);

    const handleClick = (clicked) => setIsClicked( {...initialState, [clicked]: true})
    return (
        <StateContext.Provider value={{isClicked, handleClick,
        scheduleTime, setScheduleTime, profile, setprofile,
        login, setLogin,chats, setChats,hour, setHour, 
        minute, setMinute}}>
            {children}
        </StateContext.Provider>
    )
}

export const useStateContext = () => useContext(StateContext);

