/** @format */

import { Box, Typography, useTheme } from "@mui/material";
import moment from "moment";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { DataGrid, GridToolbar } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import Header from "../../components/Header";

const Userpage = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const { id } = useParams();
  const [user, setUser] = useState([]);

  useEffect(() => {
    async function getData() {
      const request = await fetch(`http://localhost:8000/v2/patients/${id}`);
      const parsed = await request.json();

      // Group Lab_Results objects by visit number
      const resultsByVisit = parsed.lab_results.Lab_Results.reduce(
        (acc, cur) => {
          const visitNumber = parsed.lab_results.visit[cur.visit - 1];
          if (!acc.hasOwnProperty(visitNumber)) {
            acc[visitNumber] = { Cholesterol: "N/A", Creatnine: "N/A" };
          }
          if (cur.hasOwnProperty("Cholesterol")) {
            acc[visitNumber].Cholesterol = cur.Cholesterol;
          }
          if (cur.hasOwnProperty("Creatnine")) {
            acc[visitNumber].Creatnine = cur.Creatnine;
          }
          return acc;
        },
        {}
      );

      // Create an array of rows for each visit number
      const userRows = parsed.lab_results.visit.map((visitNumber, index) => {
        const date = moment().subtract(index, "months").format("L");
        const cholesterol = resultsByVisit[visitNumber].Cholesterol;
        const creatnine = resultsByVisit[visitNumber].Creatnine;
        return {
          id: parsed.id,
          first_name: parsed.first_name,
          last_name: parsed.last_name,
          visit: date,
          Cholesterol: cholesterol,
          Creatnine: creatnine,
        };
      });

      setUser(userRows);
    }

    getData();
  }, [id]);

  const columns = [
    { field: "id", headerName: "ID", width: 120 },
    { field: "first_name", headerName: "First Name", width: 200 },
    { field: "last_name", headerName: "Last Name", width: 200 },
    { field: "visit", headerName: "Visit", width: 150 },
    {
      field: "Cholesterol",
      headerName: "Cholesterol",
      width: 150,
    },
    { field: "Creatnine", headerName: "Creatnine", width: 150 },
  ];

  return (
    <Box m="20px">
      <Header title="Patient View" subtitle="Managing the Patients" />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}>
        <DataGrid
          rows={user}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
        />
      </Box>
    </Box>
  );
};

export default Userpage;
