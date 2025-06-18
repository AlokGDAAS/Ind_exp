import {createSlice} from '@reduxjs/toolkit'

const loadsState =()=>{

    try {
        const serealizedState = localStorage.getItem("flashcards")
    return serealizedState ? JSON.parse(serealizedState):[]
        
    } catch (error) {
        return []
        
    }    

}

const saveState =(state)=>{
    localStorage.setItem("flashcards",JSON.stringify(state))
}

const flashCardSlice = createSlice({
    name:"flashcards",
    initialState:loadsState(),
    reducers:{
        addGroup:(state,action)=>{
            state.push({id:Date.now(), title:action.payload,cards:[]})
            saveState(state)
            
        },
        addCard:(state,action)=>{
            const {groupId, question,answer} = action.payload
            const group = state.find((g)=> g.id == groupId)
            if(group){
             group.cards.push({id:Date.now(), question:question, answer:answer})
             console.log("Group is present")
            }
            else{
                 console.log("Group is not present")

            }
            saveState(state)
        }
    }
})

export const {addGroup, addCard} = flashCardSlice.actions

export default flashCardSlice.reducer
