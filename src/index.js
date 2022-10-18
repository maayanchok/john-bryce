import React, { UseState , UseEffect} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';



const root = ReactDOM.createRoot(document.getElementById('root'));

class Ad {
    constructor(image_url, text, link){
        this.image_url=image_url;
        this.text=text;
        this.link=link;
    }
}

let ads = [
    new Ad("./1.jpg", "this ad is 1", "https://mercedes.com"),
    new Ad("./2.jpg", "this ad is 2", "https://bmw.com"),
    new Ad("./3.jpg", "this ad is 3", "https://audi.com"),
]

class AdRotator extends React.Component {
    constructor(props){
        super(props);
            this.state={
                x:0,
                ads:[]
            };
        
    }

    get_ads=() => {
        let url="http://http://127.0.0.1:5000/ads";
        let res=fetch(url);
        res.then((data) => {
            const json_response = data.json()
            json_response.then((js) =>{
                this.setState({ads: js})
            })
        })
    }
    render = () => {
        return(
            <div style={{position:'relative',
                        backgroundColor: "pink",
                        left: 300,
                        top: 400,
                        width:200,
                        height:40}}>

                <img href={this.props.ads[this.state.x].image_url} alt="stam"/>
                <h5>{this.props.ads[this.state.x].text}</h5>
                <a href={this.props.ads[this.state.x].link}>{this.props.ads[this.state.x].link}</a>

            </div>
        )
    }
    rotate = () => {       
        this.setState({
            x:this.state.x+=1
        })
      
        console.log(this.state.x)
    }
    componentDidMount = () => {
        setInterval(this.rotate, 1000)
    }
}
root.render(<AdRotator ads={ads}  />)

