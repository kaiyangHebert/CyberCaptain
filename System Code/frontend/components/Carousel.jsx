import { StatusBar } from 'expo-status-bar';
import React, {useRef, useState} from 'react';
import { StyleSheet,Dimensions, View, Text, FlatList, TouchableOpacity, Image } from 'react-native';
import carouselItem from '../data/dummy'
import tw from 'tailwind-react-native-classnames'

const {width,height} = Dimensions.get('window');
const viewConfigRef = {viewAreaCoveragePercentThreshold:95}

const Carousel = () => {
    let flatListRef = useRef()
    const [currentIndex,setCurrentIndex] = useState(0)
    const onViewRef = useRef(({changed}) => {
        if(changed[0].isViewable) {
            setCurrentIndex(changed[0].index)
        }
    })

    const scrollToIndex = (index) => {
        flatListRef.current?.scrollToIndex({animated:true,index:index})
    }

    const renderItems = ({item}) => {
        return (
        <TouchableOpacity 
        onPress={() => console.log("clicked")}
        activeOpacity={1}
        >
        <Image source={{uri:item.url}} style={styles.image} />
        <View style={styles.footer}>
            <Text style={styles.footerText}>{item.title}</Text>
        </View>
        </TouchableOpacity>
        )
    }
    return (
        <View style={tw`bg-white`}>
            <StatusBar style='auto' />

            <FlatList 
            data={carouselItem} 
            renderItem={renderItems} 
            keyExtractor={(item, index) => index.toString()}
            horizontal
            showsHorizontalScrollIndicator={false}
            pagingEnabled
            ref={(ref) => {
                flatListRef.current=ref
            }}
            style={styles.carousel}
            viewabilityConfig={viewConfigRef}
            onViewableItemsChanged={onViewRef.current}
            />
            <View style={styles.dotView}>
                {carouselItem.map(({},index) => (
                    <TouchableOpacity 
                    key={index.toString()}
                    style={[styles.circle,
                        {backgroundColor: index == currentIndex? 'black':"grey"}
                    ]} 
                    onPress={() => scrollToIndex(index)}

                    />
                ))}
            </View>
        </View>
        
    );
}

const styles = StyleSheet.create(
    {
        carousel:{
            maxHeight: 240,

        },
        image: {
            width,
            height:180,
            resizeMode:"cover",
        },
        footer:{
            flexDirection:'row',
            justifyContent:'center',
            height:50,
            paddingHorizontal:40,
            alignItems:'center',
            backgroundColor:'#000',
        },
        footerText:{
            color:"#fff",
            fontSize:18,
            fontWeight:'bold',
        },
        dotView: {
            flexDirection:"row",
            justifyContent:"center",
            //marginVertical:10,
        },
        circle:{
            width:10,
            height:10,
            backgroundColor:"grey",
            borderRadius:50,
            marginHorizontal:5,
        }
    }
)

export default Carousel;