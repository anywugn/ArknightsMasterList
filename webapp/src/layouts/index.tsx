import { Layout } from 'antd';
import { ReactNode, FC } from 'react';

const { Header, Content, Footer } = Layout;

const BasicLayout: FC<{ location: { pathname: string }, children: ReactNode }> = ( props ) => {
  const {
    location: { pathname },
    children
  } = props;

  return (
    <Layout>
      <Header>
      </Header>
      <Content style={{ padding: '0 5%' }}>
        <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
          {children}
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>Copyright © hguandl 2021.</Footer>
    </Layout>
  );
}

export default BasicLayout;
