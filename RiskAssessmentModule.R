options(repos = c(CRAN = "https://cran.rstudio.com/"))
#Age <- 70 ; CIM <- -0.9
load("modelCIMAge.RData")
if (!requireNamespace("glm.predict", quietly = TRUE)) {
  install.packages("glm.predict")
}
library(glm.predict)
riskAssessment <- function(CIM, Age) {
  request <- paste(CIM, Age, sep = ";")
  result <- glm.predict::predicts(model1, request)$mean
  return(result)
}

