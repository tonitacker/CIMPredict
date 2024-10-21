library(glm.predict) 
library(latex2exp)

rm(list = ls()) # löscht zunächst alle Einträge des Environments
# PATH.XLSX muss auf den Pfad geändert werden, in dem die Excel-Tabelle mit den Daten liegt
# Die Excel-Datei darf dabei nicht geöffnet sein.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PATH.XLSX <- "C:/Users/akrackha/OneDrive - Stryker/Dokumente/OsteoGeo/OsteoGeoDaten.xlsx"
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# lade ggplot2

library(ggplot2)
library(dplyr)
library(xlsx)



data <- read.xlsx(PATH.XLSX, sheetName = "Messwerte")
#Löschen der zweiten Kopfzeile
data <- data[-1,]
# Umwandeln der Daten ins korrekte Format
data$Fracture <- as.numeric(data$Fracture)
data$Fracture <- as.logical(data$Fracture)
data$Osteoporotic.Fracture <- as.logical(data$Osteoporotic.Fracture)
data$Osteoporotic.Fracture.factor <- as.factor(data$Osteoporotic.Fracture)
data$X.Diagnosed.Osteoporosis <- as.logical(data$X.Diagnosed.Osteoporosis)
data$Osteopenia <- as.logical(data$Osteopenia)
data$T.Score.DXA <- as.numeric(data$T.Score.DXA)
data$T.Score.QUS <- as.numeric(data$T.Score.QUS)
data$CTX <- as.numeric(data$CTX)
data$P1NP <- as.numeric(data$P1NP)
data$D44.42CaBlood <- as.numeric(data$D44.42CaBlood)
data$D44.42CaUrine <- as.numeric(data$D44.42CaUrine)

# Verdichten: Zeilen mit Age = NA werden gestrichen
data <- data %>%
  filter(!is.na(Age)) %>%
  filter(!is.na(Fracture))
rm(PATH.XLSX)

model1 <- glm( Osteoporotic.Fracture.factor ~ D44.42CaBlood + Age, data = data , family = binomial )




