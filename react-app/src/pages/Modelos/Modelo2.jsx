
import { Container } from "../../components/MLApp/container"
import { PredictionInputModelo2 } from "../../components/MLApp/predictionInputM2"
import { useState } from "react"
import { useEffect } from "react"
import styles from "./Modelos.module.css"
import { RespuestaModelo2 } from "../../components/MLApp/respuestaModelo2"

export function Modelo2(){
    let [responseAPI, setResponseAPI] = useState()
    let [inputImage, setInputImage] = useState()
    let [preview, setPreview] = useState()
    var response, image

    useEffect(() => {
        setResponseAPI(null)
        if (!inputImage) {
            setPreview(undefined)
            return
        }
        try {
            var objectURL = URL.createObjectURL(inputImage)
            setPreview(objectURL)
        }
        catch
        {
            image = null
        }
        return () => URL.revokeObjectURL(image)
     }, [inputImage])
    if (responseAPI){
        
        response = <RespuestaModelo2 response = {responseAPI}/>
        
      }else{
        response = "No Response"
        image = null

      }
    return(
        <Container title = "Redes Convolucionales">
            <div className = {styles.M2}>
                <PredictionInputModelo2 setResponseAPI={setResponseAPI} setInputImage={setInputImage}/>
                {response}
                <div className={preview? styles.inputImage: null}><img src= {preview} />
            </div>

        
        </div>
        </Container>
    )
}