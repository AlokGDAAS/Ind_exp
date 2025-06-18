import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { addCard } from '../redux/slices/FlashCardSlice'

function AddCard({groupId}) {

    const[question , setQuestion] = useState('')
    const[answer , setAnswer] = useState('')

    const dispatch = useDispatch()

    const handleSubmit = (e) =>{
        e.preventDefault()
        console.log("Hello")
        if(question && answer){

            dispatch(addCard({groupId,question,answer}))
            setQuestion('')
            setAnswer('')

        }
    }
  return (
    <div>

        <form onSubmit={handleSubmit}>
            <input 
                 type='text'
                 placeholder='question'
                 value={question}
                 onChange={(e)=>setQuestion(e.target.value)} />
            <input 
                 type='text'
                 placeholder='answer'
                 value={answer}
                 onChange={(e)=>setAnswer(e.target.value)} />

                 <button type='submit'>Add Card</button>

        </form>



    </div>
  )
}

export default AddCard