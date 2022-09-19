import styles from "./Menu.module.css"
import { useNavigate } from "react-router-dom";


export function Tab(props){
    let navigate = useNavigate()
    
    const eventTabClick = () =>{
        props.setActiveTab(props.children)
        props.onTabClick()
        navigate('/'+props.children)

    }
    return(
        <div className={props.activeTab === props.children ? styles.Tab + ' '+ styles.activeTab : styles.Tab}
        onClick = {eventTabClick}
        >
           {props.children}
        </div>
    )
}