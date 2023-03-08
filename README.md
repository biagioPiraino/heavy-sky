# Heavy Sky
Get an SMS anytime a flight deal is discovered by using Python! :airplane::snake:

## Prerequisites
1) Register on [Tequila](https://tequila.kiwi.com/portal/login) for **free** and obtain an API key by creating a _Solution_ in your account

2) Create a [Twilio](https://www.twilio.com/login) account for **free**

## How to use
1) Create an .env file in the projects' root folder containing the following variables:
<table>
  <tr>
    <th>Field</th>
  </tr>
  <tr>
    <td>TWILIO_ACCOUNT_SID</td>
  </tr>
  <tr>
    <td>TWILIO_AUTH_TOKEN</td>
  </tr>
  <tr>
    <td>SENDER_NUMBER</td>
  </tr>
  <tr>
    <td>RECEIVER_NUMBER</td>
  </tr>
  <tr>
    <td>API_ENDPOINT_PREFIX</td>
  </tr>
  <tr>
    <td>APY_KEY</td>
  </tr>  
  <tr>
    <td>
      <a href="https://www.w3schools.com/python/python_datetime.asp"> 
        DATETIME_FORMAT
      </a>
    </td>
  </tr>  
  <tr>
    <td>
      <a href="https://www.w3schools.com/python/python_datetime.asp"> 
        FLIGHT_DATE_FORMAT
      </a>
    </td>
  </tr>  
</table>

2) Define your search criteria in the _critieria.json_ file:
<table>
  <tr>
    <th>Field</th>
    <th>Data Type</th>
    <th>Format</th>
  </tr>
  <tr>
    <td>fly_from</td>
    <td>string</td>
    <td>-</td>
  </tr>
  <tr>
    <td>fly_to</td>
    <td>string</td>
    <td>-</td>
  </tr>
  <tr>
    <td>date_from</td>
    <td>string</td>
    <td>dd/MM/yyyy</td>
  </tr>
  <tr>
    <td>date_to</td>
    <td>string</td>
    <td>dd/MM/yyyy</td>
  </tr>
  <tr>
    <td>return_from</td>
    <td>string</td>
    <td>dd/MM/yyyy</td>
  </tr>
  <tr>
    <td>return_to</td>
    <td>string</td>
    <td>dd/MM/yyyy</td>
  </tr>
  <tr>
    <td>adults</td>
    <td>number</td>
    <td>-</td>
  </tr>
  <tr>
    <td>price_from</td>
    <td>number</td>
    <td>-</td>
  </tr>
  <tr>
    <td>price_to</td>
    <td>number</td>
    <td>-</td>
  </tr>
</table>

3) Run the _main.py_ script

## References
[Tequila API - Used to retrive flights data.](https://partners.kiwi.com/our-solutions/tequila/)
<span> 
  <img src="https://orbit.kiwi/brand/logo-symbol.png" width=15 height=15>
</span>

[Twilio API - Used for sending SMS.](https://www.twilio.com/docs/sms) 
<span> 
  <img src="https://static-00.iconduck.com/assets.00/twilio-icon-512x512-bm2sbpa4.png" width=15 height=15>
</span>
