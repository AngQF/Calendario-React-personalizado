const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      available_dateTime: [],
      dateSelectedTime: [],
      dateSelected: [],
    },
    actions: {
      getAvailableDateTime: async () => {
        const response = await fetch(getStore().url + "/available_datetime", {
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        });
        const data = await response.json();
        setStore({ available_dateTime: data.resp });
      },

      getAvailableTimeofDaySelected: async (date) => {
        const response = await fetch(
          getStore().url + "/available_datetime/" + date,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: "Bearer " + localStorage.getItem("token"),
            },
          }
        );
        const data = await response.json();
        setStore({ dateSelectedTime: data.resp });
      },

      setDateSelected: (date) => {
        setStore({ dateSelected: date });
      },
    },
  };
};

export default getState;
