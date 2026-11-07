import React, {useEffect, useState} from 'react';
import { AppstoreOutlined, MailOutlined, SettingOutlined } from '@ant-design/icons';
import {Menu, Spin, Alert} from 'antd';
import axios from "axios";
import CryptocurrencyCard from "./components/CryptocurrencyCard.jsx";

function getItem(label, key, icon, children, type) {
  return {
    key,
    icon,
    children,
    label,
    type,
  };
}

const App = () => {
  const [currencies, setCurrencies] = useState([])
  const [currencyId, setCurrencyId] = useState(1)
  const [currencyData, setCurrencyData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  // Environment variable for API base URL
  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8000'

  const fetchCurrencies = async () => {
    try {
      setLoading(true)
      setError(null)
      const response = await axios.get(`${API_BASE_URL}/cryptocurrencies`)
      const currenciesResponse = response.data
      const menuItems = [
        getItem('Cryptocurrency List', 'g1', null,
          currenciesResponse.map(c => {
            return {label: c.name, key: c.id}
          }),
          'group'
        )
      ]
      setCurrencies(menuItems)
    } catch (err) {
      setError('Failed to fetch cryptocurrency list')
      console.error('Error fetching currencies:', err)
    } finally {
      setLoading(false)
    }
  }

  const fetchCurrency = async () => {
    try {
      setLoading(true)
      setError(null)
      const response = await axios.get(`${API_BASE_URL}/cryptocurrencies/${currencyId}`)
      setCurrencyData(response.data)
    } catch (err) {
      setError('Failed to fetch cryptocurrency data')
      console.error('Error fetching currency:', err)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchCurrencies()
  }, []);

  useEffect(() => {
    if (currencyId) {
      fetchCurrency()
    }
  }, [currencyId]);

  const onClick = (e) => {
    setCurrencyId(e.key)
  };

  return (
    <div className="flex min-h-screen">
      <Menu
        onClick={onClick}
        style={{
          width: 256,
        }}
        defaultSelectedKeys={['1']}
        defaultOpenKeys={['sub1']}
        mode="inline"
        items={currencies}
        className="h-screen overflow-scroll"
      />
      <div className="mx-auto my-auto p-4">
        {error && <Alert message="Error" description={error} type="error" showIcon className="mb-4" />}
        {loading ? <Spin size="large" /> : currencyData ? <CryptocurrencyCard currency={currencyData}/> : null}
      </div>
    </div>
  );
};
export default App;