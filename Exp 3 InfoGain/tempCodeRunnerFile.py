frequencyHumidity = collections.Counter(data.Humidity)
    data = ['Humidity', infoGain(frequencyHumidity,data.Humidity,tot,'Humidity')]
    writer.writerow(data)