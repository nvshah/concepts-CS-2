class Tree(lifeCycle: LifeCycle): LifeCycleObserver{
    init{
        lifeCycle.addObserver(this)
    }
    
    @OnLifeCycleEvent(LifeCycle.Event.ON_PAUSE)
    fun dummyMethod(){
        Timber.i(message:"I was Called")
    }
} 