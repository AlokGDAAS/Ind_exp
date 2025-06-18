import {configureStore} from '@reduxjs/toolkit'
import flashcardReducer from './slices/FlashCardSlice'

const store = configureStore({
    reducer:{
        flashcards: flashcardReducer
    }
})

export default store