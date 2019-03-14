
// Define a new component called button-counter
Vue.component('mosaic', {
    props: {
        events: {
            type: Array
        }
    },
  data: function () {
    return {
      count: 0
    }
  },
  template: '<button v-on:click="count++">{{events.length}} Events. You clicked me {{ count }} times.</button>'
})
    /*
import React from 'react';


const borderStyle = {
    //border: '#e4dbdb',
    //borderWidth: '1px 0px 1px 0px',
    //borderStyle: 'solid',
    //borderRadius: '4px',
    //padding: '6px',
    //background: 'white',
    //maxWidth: "300px",
    //maxHeight: "104px",
    //overflow: "scroll",
    margin: "0 auto",
};

const tileWidth = 3;
const tileGap = 2;

const styles = {
  
};

const MyComponent = () => {     

    return (
        <div style = {borderStyle}>
        <svg width = {26*tileWidth*(1.9*tileGap)} height = "100">
            <MyMosaic/>
        </svg>
        </div>

    );
};

export default MyComponent;

const Day = ({day, a1h, a2h, a3h}) => {
    a1h = Math.random();
    a2h = Math.random();
    a3h = Math.random();
    //if(Math.random() < 0.9) { a1h=0;}
    //if(Math.random() < 0.9) { a2h=0;}
    //if(Math.random() < 0.9) { a3h=0;}
    let hours = [];
    let ids = [];
    let colors = ['#C93F0F', '#B3DC4A', '#6AC0FF'];
    if(a1h>0){hours.push(a1h); ids.push(0);}
    if(a2h>0){hours.push(a2h); ids.push(1);}
    if(a3h>0){hours.push(a3h); ids.push(2);}
    //console.log(day)
    let activities = hours.length;

    return (
        <g>
            {
                (activities === 0)?
                    <rect 
                    width={(3*tileWidth)} 
                    height={(3*tileWidth)} 
                    x={13} 
                    y={(tileWidth*3 + tileGap)*day} 
                    fill='black'
                    fillOpacity='0.1'
                    key={day}
                ></rect>
                :false
            }
        
            {
        hours.map((x,i)=>{
            return <rect 
                width={(3*tileWidth) / activities} 
                height={3*tileWidth} //{hours[i]} 
                x={13+(3*i*tileWidth)/activities} 
                y = {(tileWidth*3 + tileGap)*day}//y={(tileWidth*3 + tileGap)*day - hours[i]/2} 
                fill={colors[ids[i]]}
                fillOpacity={0.2 + hours[ids[i]]*hours[ids[i]]}
                key={i}
            ></rect>
        })
    }
        </g>
    )
}

const Week = ({week}) => {
    
    return (
        [...Array(7)].map((x,i)=>{
            let t = "translate(" + (week*(tileWidth*3 + tileGap)) + ", 0)";
            return (
                <g transform={t} >
                    <Day key={i} day={i} />
                </g>
            );
        })
    );
}



const MyMosaic = () => {

    var k = 0;
    return (
        [...Array(26)].map((x,i)=>{
            return (<Week key={k++} week={i} />);
        })
    );
}
*/
