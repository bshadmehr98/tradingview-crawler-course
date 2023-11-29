def tv_analysis_to_dict(analysis):
    data = {
        "moving_avg_recomendation": analysis.moving_averages["RECOMMENDATION"],
        "moving_avg_buy_count": analysis.moving_averages["BUY"],
        "moving_avg_sell_count": analysis.moving_averages["SELL"],
        "moving_avg_neutral_count": analysis.moving_averages["NEUTRAL"]
    }
    data.update(analysis.moving_averages["COMPUTE"])
    data["oscillator_recomendation"] = analysis.oscillators["RECOMMENDATION"]
    data["oscillator_buy_count"] = analysis.oscillators["BUY"]
    data["oscillator_sell_count"] = analysis.oscillators["SELL"]
    data["oscillator_neutral_count"] = analysis.oscillators["NEUTRAL"]
    data.update(analysis.oscillators["COMPUTE"])
    
    data["high"] = analysis.indicators["high"]
    data["low"] = analysis.indicators["low"]
    data["open"] = analysis.indicators["open"]
    data["close"] = analysis.indicators["close"]
    return data