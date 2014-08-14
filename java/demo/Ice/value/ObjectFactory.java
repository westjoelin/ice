// **********************************************************************
//
// Copyright (c) 2003-2014 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

class ObjectFactory implements Ice.ObjectFactory
{
    @Override
    public Ice.Object
    create(String type)
    {
        if(type.equals("::Demo::Printer"))
        {
            return new PrinterI();
        }

        if(type.equals("::Demo::DerivedPrinter"))
        {
            return new DerivedPrinterI();
        }

        if(type.equals("::Demo::ClientPrinter"))
        {
            return new ClientPrinterI();
        }

        assert(false);
        return null;
    }

    @Override
    public void
    destroy()
    {
        // Nothing to do
    }
}
