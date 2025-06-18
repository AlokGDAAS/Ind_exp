import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { addGroup } from '../redux/slices/FlashCardSlice'

function AddGroup() {

    const [title , setTitle] = useState('')
    const dispatch = useDispatch()
    

    const handleSubmit = (e)=>{
        e.preventDefault()
        dispatch(addGroup(title))
        console.log("title from add group ",title)
        setTitle('')
    }



  return (
    <div>
    <form onSubmit={handleSubmit}>
        <input 
             type='text'
             placeholder='title'
             value={title}
             onChange={(e)=>setTitle(e.target.value)}
             />
             <button type='submit'>Add title</button>

    </form>
        
    </div>
  )
}

export default AddGroup